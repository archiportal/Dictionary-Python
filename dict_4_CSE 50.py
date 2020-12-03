# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 15:11:49 2020

@author: ARCHISMAN ROY
"""

print("Enter three elments of the dictionary :")
x=int(input())
y=int(input())
z=int(input())
dict1={"a":x,"b":y,"c":z}
m=1
for key in dict1:    
    m=m*dict1[key]
print("Product of all:",m)