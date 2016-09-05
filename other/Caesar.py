# coding=utf-8

def xorcaesar(message,key):
	return "".join([hex(ord(x) ^ ord(key))[2:] for x in message])

def decode_xorcaesar(ciphertext,key):
	return "".join([chr(int(ciphertext[x:x+2],16) ^ ord(key)) for x in xrange(0,len(ciphertext),2)])

text = """GOVERNMENT USE: If you are acquiring this software on behalf of the U.S. government, the Government shall have only "Restricted Rights"  in the software and related documentation as defined in the Federal   Acquisition Regulations (FARs) in Clause 52.227.19 (c) (2).  If you  are acquiring the software on behalf of the Department of Defense, the  software shall be classified as "Commercial Computer Software" and the  Government shall have only "Restricted Rights" as defined in Clause  252.227-7013 (c) (1) of DFARs.  Notwithstanding the foregoing, the  authors grant the U.S. Government and others acting in its behalf  permission to use and distribute the software in accordance with the  terms specified in this license.    ----------------------------------------------------------------------   Parts of this software are based on the Tcl/Tk software copyrighted by  the Regents of the University of California, Sun Microsystems, Inc.,  and other parties. The original license terms of the Tcl/Tk software  distribution is included in the file docs/license.tcltk.   Parts of this software are based on the HTML Library software  copyrighted by Sun Microsystems, Inc. The original license terms of  the HTML Library software distribution is included in the file  docs/license.html_lib. """

print xorcaesar(text,'d')
print 
print decode_xorcaesar(xorcaesar(text,'d'),'d')