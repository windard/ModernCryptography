# coding=utf-8

import string

letter = string.lowercase

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

def decode_caesar(ciphertext):
	freq = {x:ciphertext.count(x) for x in ciphertext}
	rates = sorted(freq.iteritems(),key=lambda a:a[1],reverse=True)
	return rates

def decaesar(message,key):
	return "".join([letter[(letter.index(x) + key)%26] for x in message])

if __name__ == '__main__':
	ciphertext = "AaaebphwqvvxvvmwvvbrjeuumvlphnmlaeqnjlwkwwtjlagkorEbotwrgawxmlrlazskivfetwlalmdiineobpggyiwxnvsevhtoamkeqvaqfbxzaekzrsxfwguhqhtyzglwihqzgkjloabafivbjtayiLmbiuxhrkomwfigmknsviwaaezhphxtbwkrdeswjehihnifbrvmwvltrgmdmfvsqvavlkewxzwfrsxpebztrlknmkbwwbxtwivhcqlavilguwmkjdokzAmyqwazkmsrwuwmcyvmowxtvdluwmpeqmallhfhnjlwkwwhkltxplxrmvbrbhqikrsxpkcdwpldabguiobadwbrbhqzkxpitjlslwxkalqhywawbamldwlzwvmvxhglailflzwlwlhjwxrsxmdiltxbhqztxwwrkczhthwpwuhryxu"
	ic = concide(ciphertext)
	rates = sorted(ic.iteritems(),key=lambda a:a[1],reverse=True)
	k = rates[0][0]
	caesars = [ciphertext[x::k] for x in xrange(k)]
	alphabetrates = []
	for caesar in caesars:
		result = decode_caesar(caesar)
		alphabetrates.append(result)

	for a in alphabetrates[0][:6]:
		for b in alphabetrates[1][:6]:
			for c in alphabetrates[2][:6]:
				for d in alphabetrates[3][:6]:
					for e in alphabetrates[4][:6]:
						for f in alphabetrates[5][:6]:
							for g in alphabetrates[6][:6]:
								key = []
								key.append((ord('e') - ord(a[0]))%26)
								key.append((ord('e') - ord(b[0]))%26)
								key.append((ord('e') - ord(c[0]))%26)
								key.append((ord('e') - ord(d[0]))%26)
								key.append((ord('e') - ord(e[0]))%26)
								key.append((ord('e') - ord(f[0]))%26)
								key.append((ord('e') - ord(g[0]))%26)
								messagetext = "".join([decaesar(x.lower(),key[i%k]) for i,x in enumerate(ciphertext) ])
								if messagetext.count("the") + messagetext.count("be") + messagetext.count("and") + messagetext.count("of") > 10:
									print( str(messagetext.count("the"))+" "+str(messagetext.count("be"))+" "+str(messagetext.count("and"))+" "+messagetext)
									print key

# The Great Gatsby

# he smiled understandingly much more than understandingly it was one of those rare smiles with aquality of eternal reassurance in it which you may come across four or five times in life it faced or seemed to face the whole external world for an instantand  then concentrated on you with an irresistible prejudice in your favor it understood you just so far as you wanted to be understood believed in you  as you would like to believe in yourself and as sured you  that it had precisely the impression of you that at your best you hoped to convey 

# he smiled understandingly much more than understandingly
# it was one of those rare smiles with aquality of eternal reassurance in it
# which you may come across four or five times in life
# it faced or seemed to face the whole external world for an instantand 
# then concentrated on you with an irresistible prejudice in your favor
# it understood you just so far as you wanted to be understood believed in you 
# as you would like to believe in yourself and as sured you 
# that it had precisely the impression of you that at your best you hoped to convey
