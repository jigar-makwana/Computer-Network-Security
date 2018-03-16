import binascii

win = []
winbase = 0

flag = 1
lastsentpack = -1

corrupt = []
sendpacket = 1
#Code for checksum

def ip_checksum(methoddata):
    ind = binascii.b2a_hex(methoddata)
    posn = len(ind)-1
    strinput = ""
    i = 1
    while True:
        if i >= posn :
            break
        strinput = strinput + ind[i]
        i = i+2
    var = int(strinput,16)
    var1 = var>>4
    var1 = var1 ^ var
    var2 = var1 | 0xffff
    return var2#returns the value of csumsum


#Code for degrade

def degrade(msg):
    posn = len(msg)
    iterate1 =0
    iterate2= 0
    iterate3 =0
    seqstr = ""
    csumsm = ""
    dstr = ""
    while True:
        iterate1 = iterate1+1
        if msg[iterate1-1] != "|":
            seqstr = seqstr+msg[iterate1-1]
        else:
            iterate2=1
            break
    while True:
        iterate1 = iterate1+1
        if iterate2==1 and msg[iterate1-1] != "|":
            csumsm = csumsm+msg[iterate1-1]
        else:
            iterate3=1
            break
    while True:
        iterate1 = iterate1+1
        if iterate1-1<posn:
            dstr = dstr + msg[iterate1-1]
        else:
            break
    seq = int(seqstr)
    methcksm = int(csumsm)
    packetdata = binascii.a2b_hex(dstr)#convertshexadecimal to binari
    return seq,methcksm,packetdata



#Code create

def create(seq, methcksm, packetdata):
    seqstr = str(seq)
    csumsm = str(methcksm)
    dstr = binascii.b2a_hex(packetdata)
    msg = seqstr+"|"+csumsm+"|"+dstr

    return msg

