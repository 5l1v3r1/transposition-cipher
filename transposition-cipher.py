#!/usr/bin/python

plain_text1 = "123456"
plain_text = list(plain_text1)
key = [(0,3),(1,2), (4,5)]
counter = 0
def encryption_algo(plain_text1):
for k in key:
  temp = plain_text[k[0]]
  plain_text[k[0]] = plain_text[k[1]]
  plain_text[k[1]] = temp

return "".join(plain_text)
