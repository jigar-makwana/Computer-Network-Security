import sys
import os
import random
import math

#Code to split the data
def spliter(filename):
    f = open(filename,"rb")#opens the file in varaiable f
    i=0
    a = ''
    z = []
    while True:
        data =f.read(8)#reads 8 bits from the file
        if not data:
            f.close()#closes the file
            os.remove(filename)#remove the file from the system
            break
        z.append(data)#adds the data to the list
    return z

#Code to convert data to 64 bit message
def form(temp):
    i=0
    a = ''
    while(len(temp)<8):
        temp = temp + " "
    while(i<=7):
        data = temp[i]
        #print data
        databin = bin(ord(data))#converts the character to integer first and then to binary
        databin = databin[2:]
        if(len(databin)<8):
            j=0
            z = len(databin)
            while(j<8-z):
                databin = '0'+databin
                j = j+1
        a = databin+a
        i = i+1
    #print a

    return int(a,2)

#Code to convert 64 bit message to data
def reform(a):
    #print "a ",bin(a)
    i = 0
    mask = 0b1111111
    text = ""
    while(i<8):
        text = text+chr(mask&a)
        #print chr(mask&a)
        #print mask&a
        a = a>>8
        i = i+1
    return text

#Code to generate initial permutation
def initpermut(a):
    binary = bin(a)#Converts integer to binary
    #print binary
    binary = binary[2:]
    #print binary
    #print len(binary)
    if(len(binary)<64):
        j=0
        z = len(binary)#Returnt the length of the string
        while(j<64-z):
            binary = "0"+binary
            j = j+1
    #print len(binary)
    #print binary
    ip1 = [[58,50,42,34,26,18,10,2],
           [60,52,44,36,28,20,12,4],
           [62,54,46,38,30,22,14,6],
           [64,56,48,40,32,24,16,8],
           [57,49,41,33,25,17,9,1],
           [59,51,43,35,27,19,11,3],
           [61,53,45,37,29,21,13,5],
           [63,55,47,39,31,23,15,7]]
    i = 0
    j = 0
    temp = ''
    while(i<8):
        j=0
        while(j<8):
            z = ip1[i][j]-1
            temp = binary[63-z]+temp
            j = j+1
        i = i+1
    binary = temp
    #print binary
    #print "len in ip",len(binary)
    return int(binary,2)

#Code to generate inverse of initial permutation
def invpermut(a):
    binary = bin(a)
    #print binary
    binary = binary[2:]
    #print binary
    #print len(binary)
    if(len(binary)<64):
        j=0
        z = len(binary)
        while(j<64-z):
            binary = "0"+binary
            j = j+1
    #print len(binary)
    #print binary
    iip1 = [[40,8,48,16,56,24,64,32],
            [39,7,47,15,55,23,63,31],
            [38,6,46,14,54,22,62,30],
            [37,5,45,13,53,21,61,29],
            [36,4,44,12,52,20,60,28],
            [35,3,43,11,51,19,59,27],
            [34,2,42,10,50,18,58,26],
            [33,1,41,9,49,17,57,25]]
    i = 0
    j = 0
    temp =''
    while(i<8):
        j = 0
        while(j<8):
            z = iip1[i][j]-1
            temp = binary[63-z]+temp
            j = j+1
        i = i+1
    binary = temp
    #print binary
    #print "len in inv ",len(binary)
    return int(binary,2)

#Code for permuation choice one
def pci(key):
    rd = key
    rdbin = bin(rd)
    rdbin = rdbin[2:]
    if(len(rdbin)<64):
        j=0
        z = len(rdbin)
        while(j<64-z):
            rdbin = '0'+rdbin
            j = j+1
    #print "len of string", len(rdbin)
    #print "Key is ",rdbin
    pci1 = [[57,49,41,33,25,17,9],
            [1,58,50,42,34,26,18],
            [10,2,59,51,43,35,27],
            [19,11,3,60,52,44,36],
            [63,55,47,39,31,23,15],
            [7,62,54,46,38,30,22],
            [14,6,61,53,45,37,29],
            [21,13,5,28,20,12,4]]
    i = 0
    j = 0
    temp = ''
    while(i<8):
        j = 0
        while(j<7):
            z = pci1[i][j]-1
            temp = rdbin[63-z]+temp
            j = j+1
        i = i+1
    binary = temp
    #print binary
    #print "len in pci",len(binary)
    return int(binary, 2)

#Code for left circular shift
def leftshift(a):
    binary = bin(a)
    binary = binary[2:]
    if(len(binary)<56):
        j = 0
        z = len(binary)
        while(j<56-z):
            binary = '0'+binary
            j = j+1
    #print "len in left shift ",len(binary)
    #print binary
    #print "binary left len",len(binary[:28])
    #print "binary right len",len(binary[28:])
    lbinary = binary[:28]
    rbinary = binary[28:]
    #print lbinary
    temp = lbinary[0]
    lbinary = lbinary[1:28]+temp
    #print lbinary
    #print rbinary
    temp = rbinary[0]
    rbinary = rbinary[1:28]+temp
    #print rbinary
    binary = lbinary + rbinary
    #print binary
    return int(binary,2)

#Code for permutation choice two
def pcii(a):
    binary = bin(a)
    binary = binary[2:]
    if(len(binary)<56):
        j = 0
        z = len(binary)
        while(j<56-z):
            binary = '0'+binary
            j = j+1
    #print "len in pcii",len(binary)
    #print binary
    pcii1 = [[14,17,11,24,1,5,3,28],
             [15,6,21,10,23,19,12,4],
             [26,8,16,7,27,20,13,2],
             [41,52,31,37,47,55,30,40],
             [51,45,33,48,44,49,39,56],
             [34,53,46,42,50,36,29,32]]
    i =0
    j =0
    temp = ''
    while(i<6):
        j=0
        while(j<8):
            z = pcii1[i][j]-1
            temp = binary[55-z]+temp
            j = j+1
        i = i+1
    binary = temp
    #print binary
    return int(binary,2)

#Code for expansion
def expansion(a):
    #print "_____------"
    binary = bin(a)
    binary = binary[2:]
    if(len(binary)<32):
        j = 0
        z = len(binary)
        while(j<32-z):
            binary = '0'+binary
            j = j+1
    #print "len in expansion ",len(binary)
    #print binary
    exp1 = [[32,1,2,3,4,5],
            [4,5,6,7,8,9],
            [8,9,10,11,12,13],
            [12,13,14,15,16,17],
            [16,17,18,19,20,21],
            [20,21,22,23,24,25],
            [24,25,26,27,28,29],
            [28,29,30,31,32,1]]
    i = 0
    j = 0
    temp = ''
    while(i<8):
        j = 0
        while(j<6):
            z = exp1[i][j]-1
            temp = binary[31-z]+temp
            j = j+1
        i = i+1
    binary = temp
    #print binary
    #print len(binary)
    return int(binary , 2)

#Code for permutation function
def permfunct(a):
    binary = bin(a)
    binary = binary[2:]
    j = 0
    z = len(binary)
    while(j<32-z):
        binary = '0'+binary
        j = j+1
    #print "length in permutfunct",len(binary)
    #print binary
    permut = [[16,7,20,21,29,12,28,17],
              [1,15,23,26,5,18,31,10],
              [2,8,24,14,32,27,3,9],
              [19,13,30,6,22,11,4,25]]
    i =0
    j = 0
    per = ''
    while(i<4):
        j = 0
        while(j<8):
            z = permut[i][j]-1
            per = binary[31-z] + per
            j = j+1
        i = i+1
    #print per
    return int(per,2)






#Code for s box
def sbox(a):
    #print a
    #print bin(a)
    mask = 0b111111
    s8 = mask&a
    a = a>>6
    #print bin(a)
    s7 = mask&a
    a = a>>6
    #print bin(a)
    s6 = mask&a
    a = a>>6
    #print bin(a)
    s5 = mask&a
    a = a>>6
    #print bin(a)
    s4 = mask&a
    a = a>>6
    #print bin(a)
    s3 = mask&a
    a = a>>6
    #print bin(a)
    s2 = mask&a
    a = a>>6
    #print bin(a)
    s1 = mask&a
    i = ((s1&0b100000)>>4)|(s1&0b1)
    j = ((s1&0b011110)>>1)
    #print "i",i
    #print "j",j
    S1 = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
          [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
          [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
          [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]
    s1 = S1[i][j]
    #print s1
    i = ((s2&0b100000)>>4)|(s2&0b1)
    j = ((s2&0b011110)>>1)
    #print "i",i
    #print "j",j
    S2 = [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
          [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
          [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
          [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]
    s2 = S2[i][j]
    #print s2
    i = ((s3&0b100000)>>4)|(s3&0b1)
    j = ((s3&0b011110)>>1)
    #print "i",i
    #print "j",j
    S3 = [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
          [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
          [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
          [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]
    s3 = S3[i][j]
    #print s3
    i = ((s4&0b100000)>>4)|(s4&0b1)
    j = ((s4&0b011110)>>1)
    #print "i",i
    #print "j",j
    S4 = [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
          [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
          [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
          [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]
    s4 = S4[i][j]
    #print s4
    i = ((s5&0b100000)>>4)|(s5&0b1)
    j = ((s5&0b011110)>>1)
    #print "i",i
    #print "j",j
    S5 = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
          [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
          [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
          [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]
    s5 = S5[i][j]
    #print s5
    i = ((s6&0b100000)>>4)|(s6&0b1)
    j = ((s6&0b011110)>>1)
    #print "i",i
    #print "j",j
    S6 = [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
          [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
          [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
          [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]
    s6 = S6[i][j]
    #print s6
    i = ((s7&0b100000)>>4)|(s7&0b1)
    j = ((s7&0b011110)>>1)
    #print "i",i
    #print "j",j
    S7 = [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
          [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
          [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
          [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]
    s7 = S7[i][j]
    #print s7
    i = ((s8&0b100000)>>4)|(s8&0b1)
    j = ((s8&0b011110)>>1)
    #print "i",i
    #print "j",j
    S8 = [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
          [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
          [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
          [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
    s8 = S8[i][j]
    #print s8
    temp =''
    s = bin(s8)
    s = s[2:]
    j = 0
    while(len(s)<4):
        s = '0'+s
        j = j+1
    temp = s+temp
    #print s
    s = bin(s7)
    s = s[2:]
    j = 0
    while(len(s)<4):
        s = '0'+s
        j = j+1
    temp = s+temp
    #print s
    s = bin(s6)
    s = s[2:]
    j = 0
    while(len(s)<4):
        s = '0'+s
        j = j+1
    temp = s+temp
    #print s
    s = bin(s5)
    s = s[2:]
    j = 0
    while(len(s)<4):
        s = '0'+s
        j = j+1
    temp = s+temp
    #print s
    s = bin(s4)
    s = s[2:]
    j = 0
    while(len(s)<4):
        s = '0'+s
        j = j+1
    temp = s+temp
    #print s
    s = bin(s3)
    s = s[2:]
    j = 0
    while(len(s)<4):
        s = '0'+s
        j = j+1
    temp = s+temp
    #print s
    s = bin(s2)
    s = s[2:]
    j = 0
    while(len(s)<4):
        s = '0'+s
        j = j+1
    temp = s+temp
    #print s
    s = bin(s1)
    s = s[2:]
    j = 0
    while(len(s)<4):
        s = '0'+s
        j = j+1
    temp = s+temp
    #print s
    #print temp
    #print "len in sbox", len(temp)
    return int(temp,2)




#Code for round
def rounD(a, pcii):
    binary = bin(a)
    binary = binary[2:]
    j = 0
    z = len(binary)
    while(j<64-z):
        binary = '0'+binary
        j = j+1
    left = binary[:32]
    right = binary[32:]
    l = int(left ,2)
    r = int(right ,2)
    temp = expansion(r)
    temp = temp^pcii
    temp = sbox(temp)
    temp = permfunct(temp)
    temp1 = r
    r = temp^l
    l = temp1
    left = bin(l)
    left = left[2:]
    j = 0
    z = len(left)
    while(j<32-z):
        left = '0'+left
        j = j+1
    right = bin(r)
    right = right[2:]
    j = 0
    z = len(right)
    while(j<32-z):
        right = '0'+right
        j = j+1
    binary = left+right
    #print binary
    return int(binary,2)#converts string to integer and then returns the integer

#Code for 32bit swap
def swap(a):
    binary = bin(a)
    binary = binary[2:]
    j = 0
    z = len(binary)
    while(j<64-z):
        binary = '0'+binary
        j = j +1
    left = binary[:32]
    right = binary[32:]
    temp = right
    right = left
    left = temp
    binary = left+right
    return int(binary,2)

#Code to generate the keyes for different rounds
def keyes(key):
    Pci = pci(key)
    Key = []
    #round 1
    Lc = leftshift(Pci)
    Key.append(Lc)
    #round 2
    Lc = leftshift(Lc)
    Key.append(Lc)
    #round 3
    Lc = leftshift(Lc)
    Lc = leftshift(Lc)
    Key.append(Lc)
    #round 4
    Lc = leftshift(Lc)
    Lc = leftshift(Lc)
    Key.append(Lc)
    #round 5
    Lc = leftshift(Lc)
    Lc = leftshift(Lc)
    Key.append(Lc)
    #round 6
    Lc = leftshift(Lc)
    Lc = leftshift(Lc)
    Key.append(Lc)
    #round 7
    Lc = leftshift(Lc)
    Lc = leftshift(Lc)
    Key.append(Lc)
    #round 8
    Lc = leftshift(Lc)
    Lc = leftshift(Lc)
    Key.append(Lc)
    #round 9
    Lc = leftshift(Lc)
    Key.append(Lc)
    #round 10
    Lc = leftshift(Lc)
    Lc = leftshift(Lc)
    Key.append(Lc)
    #round 11
    Lc = leftshift(Lc)
    Lc = leftshift(Lc)
    Key.append(Lc)
    #round 12
    Lc = leftshift(Lc)
    Lc = leftshift(Lc)
    Key.append(Lc)
    #round 13
    Lc = leftshift(Lc)
    Lc = leftshift(Lc)
    Key.append(Lc)
    #round 14
    Lc = leftshift(Lc)
    Lc = leftshift(Lc)
    Key.append(Lc)
    #round 15
    Lc = leftshift(Lc)
    Lc = leftshift(Lc)
    Key.append(Lc)
    #round 16
    Lc = leftshift(Lc)
    Key.append(Lc)
    #print len(Key)
    #print Key
    return Key

#Code for encryption
def Enc(temp,key):
    Ip = initpermut(temp)
    #print ">>>>>>>>>>>>>>>>>>>THE KEY ",key
    Key = keyes(key)
    #round 1
    Pcii = pcii(Key[0])
    temp = rounD(Ip,Pcii)
    #round 2
    Pcii = pcii(Key[1])
    temp = rounD(temp, Pcii)
    #round 3
    Pcii = pcii(Key[2])
    temp = rounD(temp, Pcii)
    #round 4
    Pcii = pcii(Key[3])
    temp = rounD(temp, Pcii)
    #round 5
    Pcii = pcii(Key[4])
    temp = rounD(temp, Pcii)
    #round 6
    Pcii = pcii(Key[5])
    temp = rounD(temp, Pcii)
    #round 7
    Pcii = pcii(Key[6])
    temp = rounD(temp, Pcii)
    #round 8
    Pcii = pcii(Key[7])
    temp = rounD(temp, Pcii)
    #round 9
    Pcii = pcii(Key[8])
    temp = rounD(temp, Pcii)
    #round 10
    Pcii = pcii(Key[9])
    temp = rounD(temp, Pcii)
    #round 11
    Pcii = pcii(Key[10])
    temp = rounD(temp, Pcii)
    #round 12
    Pcii = pcii(Key[11])
    temp = rounD(temp, Pcii)
    #round 13
    Pcii = pcii(Key[12])
    temp = rounD(temp, Pcii)
    #round 14
    Pcii = pcii(Key[13])
    temp = rounD(temp, Pcii)
    #round 15
    Pcii = pcii(Key[14])
    temp = rounD(temp, Pcii)
    #round 16
    Pcii = pcii(Key[15])
    temp = rounD(temp, Pcii)
    temp = swap(temp)
    temp = invpermut(temp)
    return temp

#Code for decrypt
def Dec(temp,key):
    Ip = initpermut(temp)
    #print ">>>>>>>>>>>>>", key
    Key = keyes(key)
    #round 1
    Pcii = pcii(Key[15])
    temp = rounD(Ip,Pcii)
    #round 2
    Pcii = pcii(Key[14])
    temp = rounD(temp, Pcii)
    #round 3
    Pcii = pcii(Key[13])
    temp = rounD(temp, Pcii)
    #round 4
    Pcii = pcii(Key[12])
    temp = rounD(temp, Pcii)
    #round 5
    Pcii = pcii(Key[11])
    temp = rounD(temp, Pcii)
    #round 6
    Pcii = pcii(Key[10])
    temp = rounD(temp, Pcii)
    #round 7
    Pcii = pcii(Key[9])
    temp = rounD(temp, Pcii)
    #round 8
    Pcii = pcii(Key[8])
    temp = rounD(temp, Pcii)
    #round 9
    Pcii = pcii(Key[7])
    temp = rounD(temp, Pcii)
    #round 10
    Pcii = pcii(Key[6])
    temp = rounD(temp, Pcii)
    #round 11
    Pcii = pcii(Key[5])
    temp = rounD(temp, Pcii)
    #round 12
    Pcii = pcii(Key[4])
    temp = rounD(temp, Pcii)
    #round 13
    Pcii = pcii(Key[3])
    temp = rounD(temp, Pcii)
    #round 14
    Pcii = pcii(Key[2])
    temp = rounD(temp, Pcii)
    #round 15
    Pcii = pcii(Key[1])
    temp = rounD(temp, Pcii)
    #round 16
    Pcii = pcii(Key[0])
    temp = rounD(temp, Pcii)
    temp = swap(temp)
    temp = invpermut(temp)
    return temp

#Code for Main
filename = "Example.txt"
mode = raw_input("Send 1 for EBC mode \nSend 2 for CBC mode \n>>>  ")
ER_DR = raw_input("Send 1 if you want to encrypt \nSend 2 for decrypting \n>>>  ")
things = raw_input("Send 1 for encrypting file\nSend 2 for encrypting Text\n>>>  ")
k = raw_input("Enter Encryption key:\n>>>  ")
if mode =="2":
    iv = raw_input("Enter Initialization Vector:\n>>>  ") #Initialization Vector (IV)
    IV = int(iv)
if ER_DR == "1":

    if things == '1':
        with open("123.bmp", "rb") as file:
            charac = file.read()
    if things == '2':
        charac = raw_input("Enter Text you want to encrypt\n>>>  ")
    f = open(filename,"w")
    f.write(charac)
    f.close()
#if(thing=="1"):
    alist = spliter(filename)
    if things == '2':
        f = open("encrypt.txt","w")
    if things == '1':
        f = open("encrypt.bmp","w")
    d =0
    while(d<len(alist)):
        if mode=="2":
            temp = form(alist[d])^IV
        else:
            temp = form(alist[d])
        temp = Enc(temp, int(k))
        IV = temp
        a = bin(temp)
        a = '0'+a[2:]
        i = 0
        b = int(a, 2)
        z = ''
        while(i<=7):
            mask = 0b11111111
            temp = mask&b
            b = b>>8
            #print chr(temp)
            z = chr(temp)+z
            #print bin(temp)
            i =i+1
        #print z
        f.write(z)
        d = d+1
    f.close()
    print "encryption ended"
if(ER_DR=="2"):
    #things = raw_input("Send 1 for dencrypting file\nSend 2 for dencrypting Text\n>>>  ")
    if things == "2":
        f = open("encrypt.txt", "rb")
    if things == "1":
        f = open("encrypt.bmp","rb")
    tstr = ''
    while 1:
        tempstr = f.read(8)
        if not tempstr:
            f.close()
            break
        while(len(tempstr)<8):
            tempstr = tempstr + " "
        #print tempstr
        i = 0
        g = ''
        while(i<=7):
            e = bin(ord(tempstr[i]))
            e = e[2:]
            while(len(e)<8):
                e = '0'+e
            g = g + e
            i = i+1
        temp = int(g, 2)
        var = temp
        if mode=="2":
            temp = Dec(temp, int(k))^IV
        else:
            temp = Dec(temp, int(k))
        IV = var
        text = reform(temp)
        #print text
        tstr = tstr+ text
    print tstr

    if things == '2':
        f = open("decrypt.txt","w")
    if things == '1':
        f = open("decrypt.bmp","wb")

    #f = open("decrypt.txt","w")
    f.write(tstr)
    f.close()
    print "decryption ended"
