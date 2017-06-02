# -*- coding: utf-8 -*-
"""
Created on Sun Apr 02 15:38:40 2017

@author: Yamuna
"""
import random
print "---------Diffie Hellman Key exchange---------\n"
p= int(raw_input("Enter value of 'p': "))
g= int(raw_input("Enter value of 'g': "))
sa=random.randrange(5, 50) 
sb=random.randrange(2, 30) 
print "Exhanging p & g values: ", p," & ",g,"\n"
print "Selecting random values SA & SB:", sa," & ",sb
ta=int((g**sa)%p)
tb=int((g**sb)%p)
print "Exhanging computed TA & TB values: ", ta," & ",tb,"\n"

ska=int((tb**sa)%p)
print "Secret key computed by Alice :",ska
skb=int((ta**sb)%p)
print "Secret key computed by Bob :",skb,"\n"

if ska == skb:
    print "Secret key exchanged successfully !!!"
