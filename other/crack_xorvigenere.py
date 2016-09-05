# coding=utf-8

text = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,. "

def concide(ciphertext):
	ic = {}
	for x in xrange(2,11):
		ic[x] = []
		for y in xrange(x):
			item = ciphertext[y::x]
			rates = sum([(float(item.count(z))/float(len(item)))**2 for z in set(item)])
			ic[x].append(rates)
		ic[x] = sum(ic[x])/len(ic[x])
	return ic
	
def decode_caesra(ciphertext,key):
	res = ""
	for x in ciphertext:
		char = chr(ord(x) ^ key)
		if char  not in text:
			return 
		res += char
	return key,ciphertext.encode("hex"),res

def decode_xorvigenere(ciphertext,key):
	key = key.decode("hex")
	return "".join([chr(ord(x) ^ ord(key[i%len(key)])) for i,x in enumerate(ciphertext)])

if __name__ == '__main__':
	ciphertext =  "F96DE8C227A259C87EE1DA2AED57C93FE5DA36ED4EC87EF2C63AAE5B9A7EFFD673BE4ACF7BE8923CAB1ECE7AF2DA3DA44FCF7AE29235A24C963FF0DF3CA3599A70E5DA36BF1ECE77F8DC34BE129A6CF4D126BF5B9A7CFEDF3EB850D37CF0C63AA2509A76FF9227A55B9A6FE3D720A850D97AB1DD35ED5FCE6BF0D138A84CC931B1F121B44ECE70F6C032BD56C33FF9D320ED5CDF7AFF9226BE5BDE3FF7DD21ED56CF71F5C036A94D963FF8D473A351CE3FE5DA3CB84DDB71F5C17FED51DC3FE8D732BF4D963FF3C727ED4AC87EF5DB27A451D47EFD9230BF47CA6BFEC12ABE4ADF72E29224A84CDF3FF5D720A459D47AF59232A35A9A7AE7D33FB85FCE7AF5923AA31EDB3FF7D33ABF52C33FF0D673A551D93FFCD33DA35BC831B1F43CBF1EDF67F0DF23A15B963FE5DA36ED68D378F4DC36BF5B9A7AFFD121B44ECE76FEDC73BE5DD27AFCD773BA5FC93FE5DA3CB859D26BB1C63CED5CDF3FE2D730B84CDF3FF7DD21ED5ADF7CF0D636BE1EDB79E5D721ED57CE3FE6D320ED57D469F4DC27A85A963FF3C727ED49DF3FFFDD24ED55D470E69E73AC50DE3FE5DA3ABE1EDF67F4C030A44DDF3FF5D73EA250C96BE3D327A84D963FE5DA32B91ED36BB1D132A31ED87AB1D021A255DF71B1C436BF479A7AF0C13AA14794".decode("hex")
	ic = concide(ciphertext)
	rates = sorted(ic.iteritems(),key=lambda a:a[1],reverse=True)
	k = rates[0][0]
	caesars = [ciphertext[x::k] for x in xrange(k)]
	key = ""
	for caesar in caesars:
		for x in xrange(256):
			result = decode_caesra(caesar,x)
			if result:
				key += hex(result[0])[2:]
	plaintext = decode_xorvigenere(ciphertext,key)
	print plaintext

# Cryptography is the practice and study of techniques for, among other things, secure communication in the presence of attackers. Cryptography has been used for hundreds, if not thousands, of years, but traditional cryptosystems were designed and evaluated in a fairly ad hoc manner. For example, the Vigenere encryption scheme was thought to be secure for decades after it was invented, but we now know, and this exercise demonstrates, that it can be broken very easily.
