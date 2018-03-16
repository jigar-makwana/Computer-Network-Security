import time
import binascii
import sys
import socket
import json
import random
from common import ip_checksum, degrade, create
from sys import argv



#Code to collect the file

def getfile():
    global name
    global win
    getloop = 0
    f = open(name,"wb")
    while True:
        if getloop>=len(win):
            print "loop breaking"
            break
        f.write(win[getloop])
        #print "written"
        getloop = getloop + 1
    f.close()
    print "file terminated"


    
#Code for the get pack and send pack

def servergetsend():
    global nwksocket
    global nwkname
    global nwkport
    global win
    global winbase
    global msg
    global corrupt
    global inputd
    i = 0
    sendhpacket = 1
    
    while True:
        
        sendhpacket = 1
        ackcksm = ip_checksum(binascii.a2b_hex("1234"))
        msg,address = nwksocket.recvfrom(20000)
        if msg == "!@#$%":
            print msg
            print "loop is broken"
            getfile()
            break
        seq,cksmrcv,d = degrade(msg)

        cksm = ip_checksum(d)

        if seq == winbase and cksm == cksmrcv:
            if i==len(corrupt):
                i = 0
            if inputd == "2" and corrupt[i]==seq:
                ackcksm = 1234567890
                i = i + 1
                #print "-----Ack error-----"
            if inputd == "4" and corrupt[i]==seq:
                sendhpacket = 0
                #print "-----Ack loss-----"
                i = i + 1
            msg = create(winbase, ackcksm, binascii.a2b_hex("1234"))
            if sendhpacket == 1:
                nwksocket.sendto(msg,(nwkname,nwkport))
                #print "ack sent"
            winbase = seq + 1
            win.append(d)

            
            

#Initialization

nwkname = socket.gethostname()
nwkport = 5057
onwkport = 5056
nwksocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
nwksocket.bind((nwkname, onwkport))
print "Receiver is waiting..."
win = []
winbase = 0
winend = 4
flag = 0
#dp = 1
msg = ""
ackmsg = ""
breaker = 0
name = argv [1]



#Code for main
inputd, address = nwksocket.recvfrom(2000)
error, address = nwksocket.recvfrom(5000)
corrupt = json.loads(error)
#print corrupt

servergetsend()




