# coding=utf-8

line = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

text = "abcasdsssef"

def encodebase(text):
    bintext = ""
    for x in xrange(len(text)):
        bintext += "%08d"%(int(bin(ord(text[x]))[2:]))

    print bintext

    if len(text)%3==0:
        crypto = ""
        for x in xrange(0,len(bintext),6):
            crypto += line[int(bintext[x:x+6],2)]
        print crypto
    elif len(text)%3==1:
        bintext += "0000"
        crypto = ""
        for x in xrange(0,len(bintext),6):
            crypto += line[int(bintext[x:x+6],2)]
        crypto += "=="
        print crypto
    else:
        bintext += "00"
        crypto = ""
        for x in xrange(0,len(bintext),6):
            crypto += line[int(bintext[x:x+6],2)]
        crypto += "="
        print crypto

def decodebase(cryptotext1):
    if cryptotext1.endswith("=="):
        cryptotext = cryptotext1[:-2]
    elif cryptotext1.endswith("="):
        cryptotext = cryptotext1[:-1]
    bintext = ""
    for x in xrange(len(cryptotext)):
        bintext += "%06d"%(int(bin(line.index(cryptotext[x]))[2:]))

    if cryptotext1.endswith("=="):
        bintext = bintext[:-4]
    elif cryptotext1.endswith("="):
        bintext  = bintext[:-2]
    plaintext = ""
    for x in xrange(0,len(bintext),8):
        plaintext += chr(int(bintext[x:x+8],2))

    return plaintext
if __name__ == '__main__':
    print decodebase("YWJjYXNkc3NzZWY=")
