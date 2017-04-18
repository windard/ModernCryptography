# coding=utf-8

text = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def encodebase(plaintext):
    bintext = "".join(["%08d"%(int(bin(ord(plaintext[x]))[2:])) for x in xrange(len(plaintext))])

    if len(plaintext)%3==0:
        ciphertext = "".join([text[int(bintext[x:x+6],2)] for x in xrange(0,len(bintext),6)])
    elif len(plaintext)%3==1:
        bintext += "0000"
        ciphertext = "".join([text[int(bintext[x:x+6],2)] for x in xrange(0,len(bintext),6)])
        ciphertext += "=="
    else:
        bintext += "00"
        ciphertext = "".join([text[int(bintext[x:x+6],2)] for x in xrange(0,len(bintext),6)])
        ciphertext += "="

    return ciphertext

def decodebase(ciphertext):
    cryptotext = ciphertext.replace("=","")

    bintext = "".join(["%06d"%(int(bin(text.index(cryptotext[x]))[2:])) for x in xrange(len(cryptotext))])

    if ciphertext.endswith("=="):
        bintext = bintext[:-4]
    elif ciphertext.endswith("="):
        bintext  = bintext[:-2]

    plaintext = "".join([chr(int(bintext[x:x+8],2)) for x in xrange(0,len(bintext),8)])

    return plaintext

if __name__ == '__main__':
    print encodebase("YWJjYXNkc3")
    print decodebase(encodebase("YWJjYXNkc3"))
