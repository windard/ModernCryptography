# coding=utf-8

import string

letter = string.lowercase
letterrates = {'a' : 8.167 , 'b' : 1.492 , 'c' : 2.782 , 'd' : 4.253 , 'e' : 12.702, 'f' : 2.228 , 'g' : 2.015 , 'h' : 6.094 , 'i' : 6.966 , 'j' : 0.153 , 'k' : 0.772 , 'l' : 4.025 , 'm' : 2.406 , 'n' : 6.749 , 'o' : 7.507 , 'p' : 1.929 , 'q' : 0.095 , 'r' : 5.987 , 's' : 6.327 , 't' : 9.056 , 'u' : 2.758 , 'v' : 0.978 , 'w' : 2.360 , 'x' : 0.150 , 'y' : 1.974 , 'z' : 0.074}

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

def decaesar(message,key):
    return "".join([letter[(letter.index(x) + key)%26] for x in message])

if __name__ == '__main__':
    ciphertext = "AaaebphwqvvxvvmwvvbrjeuumvlphnmlaeqnjlwkwwtjlagkorEbotwrgawxmlrlazskivfetwlalmdiineobpggyiwxnvsevhtoamkeqvaqfbxzaekzrsxfwguhqhtyzglwihqzgkjloabafivbjtayiLmbiuxhrkomwfigmknsviwaaezhphxtbwkrdeswjehihnifbrvmwvltrgmdmfvsqvavlkewxzwfrsxpebztrlknmkbwwbxtwivhcqlavilguwmkjdokzAmyqwazkmsrwuwmcyvmowxtvdluwmpeqmallhfhnjlwkwwhkltxplxrmvbrbhqikrsxpkcdwpldabguiobadwbrbhqzkxpitjlslwxkalqhywawbamldwlzwvmvxhglailflzwlwlhjwxrsxmdiltxbhqztxwwrkczhthwpwuhryxu".lower()
    # ciphertext = "tigdpruuduthibgziovhrygaiwgeptyzonvkiigfsxguiquugftrjykueoflrlcptiodksomidgqxjblnjpjwtljostxkfzldqkqoxqpetvkimautjpjwjgzooydwtblrxkwlmubneudrimbntrxxfchygquwndtoovkwynlvjphcfxksxguigazybidmsgztigziqrvrhcqmekkfbtpiwyarfcwiizoejtymskzaofwljsvrfndgpgkajulgfruejikftxzhvtumjjaoeqwljvyuokqkynlytjryqjoawggsskpnoqyirhlr"
    ic = concide(ciphertext)
    rates = sorted(ic.iteritems(),key=lambda a:a[1],reverse=True)
    k = rates[0][0]
    caesars = [ciphertext[x::k] for x in xrange(k)]
    key = []
    for caesar in caesars:
        freq = {x:caesar.count(x) for x in caesar}
        rates = sorted(freq.iteritems(),key=lambda a:a[1],reverse=True)
        alphabetnums = sum([y[1] for y in rates])
        alphabetic = {z:sum([letterrates[letter[(letter.index(y[0])+z)%26]]*y[1]/alphabetnums/100 for y in rates]) for z in xrange(26)}
        alphabetrates = sorted(alphabetic.iteritems(),key=lambda a:a[1],reverse=True)
        key.append(alphabetrates[0][0])
    messagetext = "".join([decaesar(x.lower(),key[i%k]) for i,x in enumerate(ciphertext) ])
    print messagetext

    # for a in alphabetrates[0][:6]:
    #     for b in alphabetrates[1][:6]:
    #         for c in alphabetrates[2][:6]:
    #             for d in alphabetrates[3][:6]:
    #                 for e in alphabetrates[4][:6]:
    #                     for f in alphabetrates[5][:6]:
    #                         for g in alphabetrates[6][:6]:
    #                             for h in alphabetrates[7][:6]:
    #                                 key = []
    #                                 key.append((ord('e') - ord(a[0]))%26)
    #                                 key.append((ord('e') - ord(b[0]))%26)
    #                                 key.append((ord('e') - ord(c[0]))%26)
    #                                 key.append((ord('e') - ord(d[0]))%26)
    #                                 key.append((ord('e') - ord(e[0]))%26)
    #                                 key.append((ord('e') - ord(f[0]))%26)
    #                                 key.append((ord('e') - ord(g[0]))%26)
    #                                 key.append((ord('e') - ord(h[0]))%26)
    #                                 messagetext = "".join([decaesar(x.lower(),key[i%k]) for i,x in enumerate(ciphertext) ])
    #                                 if messagetext.count("the") + messagetext.count("be") + messagetext.count("and")  > 10:
    #                                     print( str(messagetext.count("the"))+" "+str(messagetext.count("be"))+" "+str(messagetext.count("and"))+" "+messagetext)
    #                                     print key

# the almond tree was intentative blossom the days were longer often ending with magnificent evenings of corrugated pink skies the hunting season was over with hounds and guns put away for six months the vineyards were busy againas the well organized farmers treated their vines and the more lackadaisical neighbors hurried to do the pruning they should have done in november

# the almond tree was intentative blossom
# the days were longer often ending with magnificent
# evenings of corrugated pink skies the hunting
# season was over with hounds and guns put away for six months
# the vineyards were busy againas the well organized farmers treated their vines
# and the more lackadaisical neighbors hurried to do the pruning
# they should have done in november
