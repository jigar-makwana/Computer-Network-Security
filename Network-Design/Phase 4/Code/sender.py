from socket import socket, AF_INET, SOCK_DGRAM, timeout
from sys import argv
from common import ip_checksum
import matplotlib.pyplot as plt
import time

SEGMENT_SIZE = 1000

if __name__ == "__main__":
    dest_addr = argv[1]
    dest_port = int(argv[2])
    dest = (dest_addr, dest_port)
    listen_addr = argv[3]
    listen_port = int(argv[4])
    listen = (listen_addr, listen_port)
    filename = argv[5]

    with open(filename,"rb") as f:
        content = f.read()

    send_sock = socket(AF_INET, SOCK_DGRAM)
    recv_sock = socket(AF_INET, SOCK_DGRAM)

    recv_sock.bind(listen)
    recv_sock.settimeout(0.4)

    offset = 0
    seq = 0
    n = 0
    l=[]
    l=list()
    l.append(n)
    p=int(time.time())
    m=[]
    m=list()
    m.append(0)

    #a= time.time()
    while offset < len(content):
        if offset + SEGMENT_SIZE > len(content):
            segment = content[offset:]
        else:
            segment = content[offset:offset + SEGMENT_SIZE]
        offset += SEGMENT_SIZE

        ack_received = False
        
        while not ack_received:
            send_sock.sendto(ip_checksum(segment) + str(seq) + segment, dest)

            try:
                message, address = recv_sock.recvfrom(1024)
            except timeout:
                print "Timeout"
                n = n+1
                q=int(time.time())
                print 'error count = %d at time : %d second'%(n,(q-p))
                l.extend([n])                
                m.extend([q-p])
            else:
                print message
                r=int(time.time())
                print "pkt succesfully send at %d"%(r-p)
                checksum = message[:2]
                ack_seq = message[5]
                if ip_checksum(message[2:]) == checksum and ack_seq == str(seq):
                    ack_received = True

        seq = 1 - seq

    recv_sock.close()
    """
    b= time.time()
    print "time taken :%d second"%(b-a)
    """
    plt.plot(m,l)
    plt.show()
