# coding=utf-8

# hex2base

import base64

# def hex2base(strings):
# 	text = ""
# 	for x in xrange(0,len(strings),2):
# 		text += chr(int(strings[x:x+2],16))
# 	result =  base64.b64encode(text)
# 	return result

def hex2base(strings):
	return base64.b64encode("".join([chr(int(strings[x:x+2],16)) for x in xrange(0,len(strings),2)]))

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


strings = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
print hex2base(strings)