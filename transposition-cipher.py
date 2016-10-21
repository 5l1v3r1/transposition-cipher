#!/usr/bin/python

plain_text1 = "Mohammad Askar"
plain_text = list(plain_text1)
key = [(0,3),(1,2)]
counter = 0
for k in key:
  temp = plain_text[k[0]]
  #print "temp now is equal {0}".format(temp)

  plain_text[k[0]] = plain_text[k[1]]
  #print "plain_text[k[1]] which is {0} equals plain_text[k[0]] which is {1}".format(plain_text)

  plain_text[k[1]] = temp

  #print "plain_text[k[1]] which is {0} equals temp which is {1}".format(plain_text[k[1]],temp)

print "".join(plain_text)
