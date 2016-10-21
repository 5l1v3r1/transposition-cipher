#!/usr/bin/python

plain_text1 = "My Secret !:D"
plain_text = list(plain_text1)
key = [(0,3),(1,6), (4,5), (7,9)]
counter = 0
def encryption_algo(plain_text1):
 for k in key:
  temp = plain_text[k[0]]
  plain_text[k[0]] = plain_text[k[1]]
  plain_text[k[1]] = temp
 return "".join(plain_text)

#print encryption_algo(plain_text1)

def decryption_algo(plain_text1):
 for k in key:
  temp = plain_text[k[1]]
  plain_text[k[1]] = plain_text[k[0]]
  plain_text[k[0]] = temp

 return "".join(plain_text)

cipher_text = encryption_algo(plain_text)
decrypted_text = decryption_algo(cipher_text)
print "Your Plain Text is : {0}".format(plain_text1)
print "*" * 25
print "Your Encrypted Text is : {0} ".format(cipher_text)
print "*" * 25
print "Your Decrypted Text is : {0}".format(decrypted_text)

