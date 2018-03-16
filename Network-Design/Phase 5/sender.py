import socket
import binascii
import time
import threading
import random
import json
import sys
from common import ip_checksum, create, degrade
from sys import argv

class Thread(threading.Thread):
    def __init__(self,method):
        threading.Thread.__init__(self, target = method)
        self.start()
        


#Divinding file code

def divider(name):
    f = open(name,"rb")
    wintemp = []
    loopcount = 0
    while True:
        dtemp = f.read(1024)
        if not dtemp:
            break
        wintemp.append(dtemp)
        loopcount = loopcount+1
    print "Window Length ",len(wintemp)
    f.close()
    return wintemp

#Code for error in packet

def error(per):
    global win
    vint = int(per)
    packeterror = (vint*len(win))/100
    wintemp = []
    if packeterror<=0:
        wintemp = [0xffffff]
        return wintemp
    errloop1 = 0
    errloop2 = 0
    while errloop1<=packeterror-1:
        wintemp.append(random.randrange(0,len(win)-1))
        while errloop2<errloop1:
            if wintemp[errloop1] == wintemp[errloop2]:
                del wintemp[errloop1]
                errloop1 = errloop1 - 1
            errloop2 = errloop2 + 1
        errloop1 = errloop1 + 1
        errloop2 = 0
    wintemp.sort()
    #print wintemp
    return wintemp









#Code to send packet
def clientsender():
    global nwksocket
    global nwkname
    global nwkport
    global win
    global winbase
    global winend
    global winsize
    global flag
    global lastsentpack
    global corrupt
    global inputd
    global sendpacket
    global t
    global ts
    global xx
    global yy
    lastsentpack = 0
    i = 0
    
    
    while True:
        sendpacket = 1
        ts.extend([time.time()])
        z =(ts[i] - ts[i+1])
        if z<t:
            t = z
        if lastsentpack<= winend and flag == 1 and lastsentpack<len(win):
            cksm = ip_checksum(win[lastsentpack])
            if inputd == "3" and corrupt[i]==lastsentpack:
                cksm = 0
                i = i + 1
                if i == len(corrupt):
                    i = 0
            
            if inputd == "5" and corrupt[i]==lastsentpack:
                sendpacket = 0
                i = i + 1
                if i == len(corrupt):
                    i = 0
            message = create(lastsentpack,cksm,win[lastsentpack])
            if sendpacket == 1:
                with lock:
                    nwksocket.sendto(message,(nwkname,nwkport))
                    
            lastsentpack = lastsentpack + 1
            tt= int(time.time())
            ts.extend([tt])
        if winbase == len(win) and lastsentpack == len(win):
            print "sender broken"
            break


#Code to get the d
def clientgot():
    global nwksocket
    global win
    global winbase
    global winend
    global winsize
    global inputd
    global corrupt
    global flag
    global lastsentpack
    global sendpacket
    global start
    global s
    global t
    global ts
    seq = 0
        
    while True:
        
        try:
            ackmsg,address = nwksocket.recvfrom(2500)
        except:
            winsize=winsize-1
            with lock:
                lastsentpack = winbase
                flag = 1
        else:
            with lock:
                flag = 0
            seq,cksmrcv,ack = degrade(ackmsg)
            cksm = ip_checksum(ack)
            if seq>=winbase and cksm == cksmrcv:
                
                if winsize<20:
                    winsize=winsize+1
                   
                ts.extend([time.time()])
                with lock:
                    winbase = seq + 1
                    winend = winsize + winbase

                if winend>=len(win):
                    winend = len(win)-1
                flag = 1
            else:
                winsize=winsize-1
                with lock:
                    winbase = seq
                    lastsentpack = winbase
                    flag = 1
        if seq == len(win)-1:
            with lock:
                sendpacket = 0

                nwksocket.sendto("!@#$%",(nwkname,nwkport))
                nwksocket.close()
                end = time.time()
                print "time to implement is ",end-start
                #print ts
                #print (ts[win-1]-ts[win])
                print winsize
                break
                




    


#Initialization 

nwkname = socket.gethostname()
nwkport = 5056
onwkport = 5057
nwksocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
nwksocket.bind((nwkname, onwkport))
t=0.4
nwksocket.settimeout(t)
ts=[]
ts=list()
ts.append(time.time())
s=0
xx=0
yy=0
print "Sender is waiting..."
win = []
winbase = 0
strsize = raw_input("Enter window size")
winsize = int(strsize)-1
winend = winsize
slider = winend - winbase
flag = 1
lastsentpack = -1
lock = threading.Lock()
name = argv [1]
corrupt = []
sendpacket = 1
#Code Options
inputd = raw_input("Option 1 - no loss\n" "Option 2 - ACK packet bit-error\n" "Option 3 - Data packet bit-error\n" "Option 4 - ACK packet loss\n" "Option 5 - Data packet loss\n")


#Code for main

win = divider(name)
#print "window"
if inputd != "1":
    nwksocket.sendto(inputd,(nwkname,nwkport))
    percentage = raw_input("Enter error %\n")
    corrupt = error(percentage)
    nwksocket.sendto(json.dumps(corrupt),(nwkname,nwkport))
    
else:
    nwksocket.sendto(inputd,(nwkname,nwkport))
    corrupt = [0xffffff]
    nwksocket.sendto(json.dumps(corrupt),(nwkname,nwkport))
    

start = int(time.time())
print "Start time :",start

Thread(clientsender)
Thread(clientgot)
