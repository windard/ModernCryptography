# coding=utf-8

text='abcdefghijklmnopqrstuvwxyz'

def vigenere(message,key):
	return "".join([text[(text.index(x) + text.index(key[i % len(key)]))%26] for i,x in enumerate(message)])

def decode_vigenere(cryptotext,key):
	return "".join([text[(text.index(x) - text.index(key[i % len(key)]))%26] for i,x in enumerate(cryptotext)])

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

def crack_vigenere(ciphertext):
	ic = concide(ciphertext)
	rates = sorted(ic.iteritems(),key=lambda a:a[1],reverse=True)
	k = rates[0][0]
	caesars = [ciphertext[x::k] for x in xrange(k)]
	key = ""
	for caesar in caesars:
		rates = {x:caesar.count(x) for x in set(caesar)}
		rates = sorted(rates.iteritems(),key=lambda a:a[1],reverse=True)
		key += text[(text.index(rates[0][0]) - text.index('e'))%26]
	plaintext = decode_vigenere(ciphertext,key)
	return key,plaintext

if __name__ == '__main__':
	# plaintext = "Nothing in this License Agreement shall be deemed to create anyrelationship of agency partnership or joint venture between PSF andLicensee  This License Agreement does not grant permission to use PSFtrademarks or trade name in a trademark sense to endorse or promoteproducts or services of Licensee or any third party PSF is making Python available to Licensee on an AS IS basis  PSF MAKES NO REPRESENTATIONS OR WARRANTIES EXPRESS OR IMPLIED  BY WAY OF EXAMPLE BUT NOT LIMITATION PSF MAKES NO AND DISCLAIMS ANY REPRESENTATION OR WARRANTY OF MERCHANTABILITY OR FITNESS FOR ANY PARTICULAR PURPOSE OR THAT THE USE OF PYTHON WILL NOT INFRINGE ANY THIRD PARTY RIGHTS Subject to the terms and conditions of this BeOpen Python License Agreement  BeOpen hereby grants Licensee a non exclusive  royalty free  world wide license to reproduce  analyze  test  perform and or display publicly  prepare derivative works  distribute  and otherwise use the Software alone or in any derivative version  provided  however  that the BeOpen Python License is retained in the Software  alone or in any derivative version prepared by Licensee GOVERNMENT USE If you are acquiring this software on behalf of the U S  government  the Government shall have only  Restricted Rights  in the software and related documentation as defined in the Federal  Acquisition Regulations  FARs  in Clause  If you are acquiring the software on behalf of the Department of Defense  the software shall be classified as  Commercial Computer Software  and the Government shall have only  Restricted Rights  as defined in Clause of DFARs   Notwithstanding the foregoing  the authors grant the U S  Government and others acting in its behalf permission to use and distribute the software in accordance with the terms specified in this license  THE AUTHORS AND DISTRIBUTORS SPECIFICALLY DISCLAIM ANY WARRANTIES INCLUDING  BUT NOT LIMITED TO  THE IMPLIED WARRANTIES OF MERCHANTABILITY FITNESS FOR A PARTICULAR PURPOSE  AND NON INFRINGEMENT IS PROVIDED ON AN  AS IS  BASIS  AND THE AUTHORS AND DISTRIBUTORS HAVENO OBLIGATION TO PROVIDE MAINTENANCE  SUPPORT  UPDATES  ENHANCEMENTS  ORMODIFICATIONS OVERNMENT USE If you are acquiring this software on behalf of theU S  government  the Government shall have only  Restricted Rights in the software and related documentation as defined in the FederalAcquisition Regulations  FAR  in Clause are acquiring the software on behalf of the Department of Defense  thesoftware shall be classified as  Commercial Computer Software  and theGovernment shall have only  Restricted Rights  as defined in Clauseauthors grant the U S  Government and others acting in its behalfpermission to use and distribute the software in accordance with theterms specified in this license The authors hereby grant permission to use  copy  modify  distribute and license this software and its documentation for any purpose  providedthat existing copyright notices are retained in all copies and that thisnotice is included verbatim in any distributions  No written agreement license  or royalty fee is required for any of the authorized uses Modifications to this software may be copyrighted by their authorsand need not follow the licensing terms described here  provided thatthe new terms are clearly indicated on the first page of each file wherethey apply Nothing in this License Agreement shall be deemed to create anyrelationship of agency partnership or joint venture between PSF andLicensee  This License Agreement does not grant permission to use PSFtrademarks or trade name in a trademark sense to endorse or promoteproducts or services of Licensee or any third party PSF is making Python available to Licensee on an AS IS basis  PSF MAKES NO REPRESENTATIONS OR WARRANTIES EXPRESS OR IMPLIED  BY WAY OF EXAMPLE BUT NOT LIMITATION PSF MAKES NO AND DISCLAIMS ANY REPRESENTATION OR WARRANTY OF MERCHANTABILITY OR FITNESS FOR ANY PARTICULAR PURPOSE OR THAT THE USE OF PYTHON WILL NOT INFRINGE ANY THIRD PARTY RIGHTS Subject to the terms and conditions of this BeOpen Python License Agreement  BeOpen hereby grants Licensee a non exclusive  royalty free  world wide license to reproduce  analyze  test  perform and or display publicly  prepare derivative works  distribute  and otherwise use the Software alone or in any derivative version  provided  however  that the BeOpen Python License is retained in the Software  alone or in any derivative version prepared by Licensee GOVERNMENT USE If you are acquiring this software on behalf of the U S  government  the Government shall have only  Restricted Rights  in the software and related documentation as defined in the Federal  Acquisition Regulations  FARs  in Clause  If you are acquiring the software on behalf of the Department of Defense  the software shall be classified as  Commercial Computer Software  and the Government shall have only  Restricted Rights  as defined in Clause of DFARs   Notwithstanding the foregoing  the authors grant the U S  Government and others acting in its behalf permission to use and distribute the software in accordance with the terms specified in this license  THE AUTHORS AND DISTRIBUTORS SPECIFICALLY DISCLAIM ANY WARRANTIES INCLUDING  BUT NOT LIMITED TO  THE IMPLIED WARRANTIES OF MERCHANTABILITY FITNESS FOR A PARTICULAR PURPOSE  AND NON INFRINGEMENT IS PROVIDED ON AN  AS IS  BASIS  AND THE AUTHORS AND DISTRIBUTORS HAVENO OBLIGATION TO PROVIDE MAINTENANCE  SUPPORT  UPDATES  ENHANCEMENTS  ORMODIFICATIONS OVERNMENT USE If you are acquiring this software on behalf of theU S  government  the Government shall have only  Restricted Rights in the software and related documentation as defined in the FederalAcquisition Regulations  FAR  in Clause are acquiring the software on behalf of the Department of Defense  thesoftware shall be classified as  Commercial Computer Software  and theGovernment shall have only  Restricted Rights  as defined in Clauseauthors grant the U S  Government and others acting in its behalfpermission to use and distribute the software in accordance with theterms specified in this license The authors hereby grant permission to use  copy  modify  distribute and license this software and its documentation for any purpose  providedthat existing copyright notices are retained in all copies and that thisnotice is included verbatim in any distributions  No written agreement license  or royalty fee is required for any of the authorized uses Modifications to this software may be copyrighted by their authorsand need not follow the licensing terms described here  provided thatthe new terms are clearly indicated on the first page of each file wherethey apply ".lower().replace(" ","")
	# key = "iloveyou"
	# ciphertext =  vigenere(plaintext,key)
	# key,message = crack_vigenere(ciphertext)
	# print key,message
	print vigenere("wearediscoveredsaveyourself","deceptive").upper()
