#!/usr/bin/python

plain_text1 = "abcdxxxxx"
plain_text = list(plain_text1)
key = [(0,3),(1,2), (4,5), (7,9),(5,9),(10,25)]
counter = 0
def encryption_algo(ptx):
 for k in key:
  try:
   temp = ptx[k[0]]
   ptx[k[0]] = ptx[k[1]]
   ptx[k[1]] = temp
  except:
	  pass
 return "".join(ptx)

#print encryption_algo(plain_text1)

def decryption_algo(plain_text1):
 for k in key:
  try:
   temp = plain_text[k[1]]
   plain_text[k[1]] = plain_text[k[0]]
   plain_text[k[0]] = temp
  except:
	  pass
 return "".join(plain_text)

cipher_text = encryption_algo(plain_text)
decrypted_text = decryption_algo(cipher_text)
print "Your Plain Text is : {0}".format(plain_text1)
print "*" * 25
print "Your Encrypted Text is : {0} ".format(cipher_text)
print "*" * 25
print "Your Decrypted Text is : {0}".format(decrypted_text)

