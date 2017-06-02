# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 13:23:09 2017

@author: Yamuna
"""
import re
lc = re.compile('[a-z]+')
uc = re.compile('[A-Z]+')

msg = raw_input("Enter message to be encrypted:")
key = raw_input('Enter key for Ceaser Cipher:')

#msg = 'Mark Zuckerberg'
#count = 5

print("\nEncryption using Ceaser Cipher-------->>")

k=int(key)
res=''
for i in msg:
    j=ord(i)+k
    if (lc.findall(i)) and (j>122):
            j=j-26
    if (uc.findall(i)) and (j>90):
            j=j-26
    res = res+str(chr(j))

print(res)
print("\nDecryption using Ceaser Cipher-------->>")

msg = res
res=''
for i in msg:
    j=ord(i)-k
    if (lc.findall(i)) and (j<97):
        j=j+26
    if (uc.findall(i)) and (j<65):
        j=j+26
    res = res+str(chr(j))

print res



