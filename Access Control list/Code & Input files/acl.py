# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 17:50:59 2017

@author: Yamuna
"""

import csv
import re

with open('acl.csv', 'rb') as f:
    reader = csv.reader(f)
    data = list(reader)
    
acl = iter(data)

with open('packets.csv', 'rb') as f:
    reader = csv.reader(f)
    data1 = list(reader)
    
packets = iter(data1)

line=[]
denied=[]
result=[]

for i in packets:
    acl = iter(data)
    for j in acl:
        if i[0] == j[4] and j[2] == "deny" and i[1] == j[6]:
            line.append(i)
            line.append("denied")
            line.append("for port number")
            line.append(j[8])
            for k in data:
                if j[1] in k and k[0] == "interface":
                    line.append("through")   
                    line.append(k[1])
            result.append(line)
            line=[]
            if i not in denied:
                denied.append(i)
        if i[0] == j[4] and j[2] == "deny" and j[6] == " ":
            line.append(i)
            line.append("denied")
            line.append("for all ports")
            for k in data:
                if j[1] in k and k[0] == "interface":
                    line.append("through")   
                    line.append(k[1])
            result.append(line)
            line=[]
            if i not in denied:
                denied.append(i)
        
for i in data1:
    if i not in denied:
        line.append(i)
        line.append("allowed")
        result.append(line)
        line=[]

for i in result:
    text=str(i)
    print(re.sub('[^.a-zA-Z0-9 ]+',' ', text))
