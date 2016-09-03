# coding=utf-8

def hex2num(strings1,strings2):
	text = ""
	for x in xrange(0,len(strings1),2):
		text += hex(int(strings1[x:x+2],16) ^ int(strings2[x:x+2],16))[2:]
	return text

def hex2num(strings1,strings2):
	return "".join([hex(int(strings1[x:x+2],16) ^ int(strings2[x:x+2],16))[2:] for x in xrange(0,len(strings1),2)])

strings1 = "1c0111001f010100061a024b53535009181c"
strings2 = "686974207468652062756c6c277320657965"
print hex2num(strings1,strings2)

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])