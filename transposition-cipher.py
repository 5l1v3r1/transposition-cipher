#!/usr/bin/python

plain_text1 = "Mohammad Askar"
plain_text = list(plain_text1)
key = [(0,3),(1,2)]
counter = 0
for k in key:
  temp = plain_text[k[0]]
  

  plain_text[k[0]] = plain_text[k[1]]
 

  plain_text[k[1]] = temp

 

print "".join(plain_text)
