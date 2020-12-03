# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 15:25:17 2020

@author: ARCHISMAN ROY
"""

d = {}
n=int(input("Enter the number of elements:"))
for i in range(1,n+1):
    x=str(input("Enter color:"))
    y=str(input("Enter number:"))
    d[x]=y
if not bool(d):
    print("Dictionary is empty.")
else:
    print("Not empty.")



