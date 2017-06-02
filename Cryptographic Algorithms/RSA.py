# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 18:53:08 2017

@author: Yamuna
"""
p= int(raw_input("Enter value of 'p': "))
q= int(raw_input("Enter value of 'q': "))
m= int(raw_input("Enter Message to be encrypted: "))
'''
p=11
q=17
m=5
'''

n=p*q
for i in range(5,1000):
    if (p-1)%i<>0 and (q-1)%i<>0:
        e=i
        #print "The value of 'e'",e
        break

for i in range(1000):
    if i<>e and ((e*i)%((p-1)*(q-1)) ==1):
        d=i
        #print "The value of 'd'",d
        break

print "Public Key (e,n): (",e,",",n,")"
print "Private Key (d,n): (",d,",",n,")"

c=(m**e)%n
c=int(c)
print "Encrypted cipher text :",c
m=(c**d)%n
m=int(m)
print "Decrypted plain text :",m

# Encryption and decryption using Lecture notes formula
print "\nEncryption and decryption using Lecture notes formula\n"

itr=e/2
mitr=1
for i in range(itr):
    mitr=mitr*((m**2)%n)
#    print "iter",mitr
    if e%2<>0:
        c=((mitr*(m%n))%n)
    else:
        c=(mitr%n)
print "Encrypted cipher text :",c
#print c,itr
itr=d/2
citr=1
for i in range(itr):
    citr=citr*((c**2)%n)
m=((citr*(c%n))%n)    
print "Decrypted plain text :",m
