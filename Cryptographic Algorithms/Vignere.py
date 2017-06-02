# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 17:54:53 2017

@author: Yamuna
"""

import re
lc = re.compile('[a-z]+')
uc = re.compile('[A-Z]+')

#msg = raw_input("Enter message to be encrypted:")
#key = raw_input('Enter key for Ceaser Cipher:')

msg = 'MarkZuckerberg'
key="facebook"

print("\nEncryption using Vigenere Cipher-------->>")

from itertools import cycle
map = zip(msg, cycle(key))
print "Key Mapping"
print map
res=''
for i,j in map:
    if (lc.findall(i)):
        e=(((ord(i)-97)+(ord(j)-97))%26)+97
        res = res+str(chr(e))    
  
    if (uc.findall(i)):
        e=(((ord(i)-65)+(ord(j)-97))%26)+65
        res = res+str(chr(e))        
print("\nEncrypted Result-------->>")    
print res
print("\nDecryption using Vigenere Cipher-------->>")
msg = res
map = zip(msg, cycle(key))
print "Key Mapping"
print map
res =''
for i,j in map:
    if (lc.findall(i)):
        e=(((ord(i)-97)-(ord(j)-97))%26)+97
        res = res+str(chr(e))    
  
    if (uc.findall(i)):
        e=(((ord(i)-65)-(ord(j)-97))%26)+65
        res = res+str(chr(e))    
print("\nDecrypted Result-------->>")            
print res