from socket import *
import random
import time
import os


def usage():
    print "Usage: python error.py FromSenderPort ToReceiverPort FromReceiverPort ToSenderPort"
    exit()


def randSleep():
    """
    Sleep for a uniformly random amount of time between 80 and 120ms.
    """
    #delay = random.random() * 0.0
    delay = random.random() * 0.02
    #delay = random.random() * 0.05
    #delay = random.random() * 0.09
    sign = random.randint(0, 1)
    if (sign == 1):
        delay = -delay
    delay += 0.1
    time.sleep(delay)


def corrupt(pkt):
    # corrupt a packet
    index = random.randint(0, len(pkt)-1)
    pkt = pkt[:index] + str(unichr(random.randint(0, 95))) + pkt[index+1:]
    return pkt


def intercept(pkt, outSock, addr):
    rand = random.randint(1, 10)
    if rand >= w and rand <= x:
        print "Dropped"
        return
    if rand >= y and rand <= z:
        pkt = corrupt(pkt)
        print "Corrupted to:", pkt

    
    if rand >= s and rand <= 10:
        print "sent"
    randSleep()
    outSock.sendto(pkt, addr)

from sys import argv
if len(argv) < 5:
    usage()

fromSenderAddr = ('localhost', int(argv[1]))
toReceiverAddr = ('localhost', int(argv[2]))
fromReceiverAddr = ('localhost', int(argv[3]))
toSenderAddr = ('localhost', int(argv[4]))


fromSenderSock = socket(AF_INET, SOCK_DGRAM)
fromSenderSock.bind(fromSenderAddr)
fromSenderSock.setblocking(0)
fromReceiverSock = socket(AF_INET, SOCK_DGRAM)
fromReceiverSock.bind(fromReceiverAddr)
fromReceiverSock.setblocking(0)

outSock = socket(AF_INET, SOCK_DGRAM)
print "Listening..."

print "Enter 1 for without error;\nEnter 2 for 30 per error;\n" +\
      "Enter 3 for 50 per error;\nEnter 4 for 75 per error:" 

iput=raw_input()
if iput == "1":
    print "Sending withour error\n\n\n\n\n"
    w=11
    x=12
    y=13
    z=14
    s=1
if iput == "2":
    print "Sending at 30 per error\n\n\n\n\n"
    w=1
    x=2
    y=3
    z=4
    s=5
if iput == "3":
    print "Sending at 50 per error\n\n\n\n\n"
    w=1
    x=2
    y=3
    z=5
    s=6
if iput == "4":
    print "Sending at 75 per error\n\n\n\n\n"
    w=1
    x=3
    y=4
    z=7
    s=8

while True:
    rd= random.randint(1,10)
    try:
        pkt = fromSenderSock.recv(2048)
        print "Received packet from sender:", pkt
        intercept(pkt, outSock, toReceiverAddr)
    except error:
        pass
    try:
        pkt = fromReceiverSock.recv(2048)
        print "Received packet from receiver:", pkt
        intercept(pkt, outSock, toSenderAddr)
    except error:
        pass
    
        
            
