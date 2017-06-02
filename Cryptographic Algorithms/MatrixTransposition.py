# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 18:53:08 2017

@author: Yamuna
"""
print "---------------Encryption-------------->>"
msg="matrixisverydifficulttoimplement"
key=[5,2,3,4,1]
c = len(key)
l = len(msg)
if (l%c == 0):
    r = l/c
else:
    r = (l/c)+1
a='a'     
#Encryption
mat= [[a for x in range(c)] for y in range(r)]       
matrix = list(msg)
#Padding
if l%c <> 0:
    count= (c-(l%c))
    for x in range(count):
        matrix.append('X')
for x in range(r):
    mat[x]=matrix[:c]
    matrix=matrix[c:]
for x in range(r):
    print mat[x]
res=''
for z in range(c):
    for x in range(r):
        k=key[z]-1
        res+=mat[x][k]
print "\n---------------Encrypted Cipher text--------------->>"
print res+"\n"
#Decryption
print "---------------Decryption-------------->>"
matrix = list(res)
mat= [[a for x in range(r)] for y in range(c)]
for x in range(c):
    mat[x]=matrix[:r]
    matrix=matrix[r:]
for x in range(c):
    print mat[x]
res=''
matrix= [[a for x in range(r)] for y in range(c)]       
matrix=[list(i) for i in zip(*mat)]    
for x in range(r):
    for z in range(c):
         u=key[z]-1
         res+=matrix[x][u]
#removing padding characters and printing decrypted message
print "\n---------------Decrypted message with padding--------------->>"
print res
print "---------------Decrypted message without padding--------------->>"
print res[:-count]