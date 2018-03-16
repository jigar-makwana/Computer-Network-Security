from socket import socket, AF_INET, SOCK_DGRAM
from sys import argv, stdout
from common import ip_checksum
import time

def send(content, to):
    checksum = ip_checksum(content)
    send_sock.sendto(checksum + content, to)

if __name__ == "__main__":
    dest_addr = argv[1]
    dest_port = int(argv[2])
    dest = (dest_addr, dest_port)
    listen_addr = argv[3]
    listen_port = int(argv[4])
    listen = (listen_addr, listen_port)
    filename = argv[5]

    send_sock = socket(AF_INET, SOCK_DGRAM)
    recv_sock = socket(AF_INET, SOCK_DGRAM)

    recv_sock.bind(listen)
    print "Listening...."

    expecting_seq = 0
    pk=1

    f = open(filename,'wb')

    while True:
        message, address = recv_sock.recvfrom(1024)
        print "%d pkt received"%pk
        print "at a time : " ,time.time()
        print "\n\n"
        pk = pk+1
        
        checksum = message[:2]
        seq = message[2]
        content = message[3:]

        if ip_checksum(content) == checksum:
            send("ACK" + seq, dest)

            if seq == str(expecting_seq):
                stdout.write(content)
                print "\n\n"
                expecting_seq = 1 - expecting_seq
                while(content):                    
                    f.write(content)
                    content = message[3:]
                    break
            
            else:
                negative_seq = str(1 - expecting_seq)
                send("ACK" + negative_seq, dest)

    f.close()
