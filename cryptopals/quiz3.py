# coding=utf-8

# def hex2str(strings):
# 	text = ""
# 	for x in xrange(0,len(strings),2):
# 		text += chr(int(strings[x:x+2],16))
# 	return text

def hex2str(strings):
	return "".join([chr(int(strings[x:x+2],16)) for x in xrange(0,len(strings),2)])

def hex2str(strings):
	return strings.decode("hex")

def singlexor(strings):
	cryptotext =  hex2str(strings)

	rates = {x:cryptotext.count(x) for x in set(cryptotext)}

	rates = sorted(rates.iteritems(),key=lambda a:a[1],reverse=True)

	for x in xrange(26):
		print chr(ord('a') + x),
		key = ord(rates[1][0]) ^ (ord('a') + x)
		plaintext =  "".join([chr(int(strings[y:y+2],16) ^ key) for y in xrange(0,len(strings),2)])
		for y in plaintext:
			if ord(y) < 32 or ord(y) > 126:
				break
		else:
			print plaintext

strings = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
singlexor(strings)
# o Cooking MC's like a pound of bacon
# 不是密文中词频最高的那个字母 对应 e
# 而是词频第二高的对应 o
	