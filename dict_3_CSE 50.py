# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:58:08 2020

@author: ARCHISMAN ROY
"""

dict1={"1":"23", "2":"34"}
dict2={"3":"51", "4":"42"}
dict3={"5":"64","6":"89"}
print("Dictionary 1:",dict1)
print("Dictionary 2:",dict2)
print("Dictionary 3:",dict3)
dict4 = {}
for d in (dict1, dict2, dict3): dict4.update(d)
print("Dictionary 4 after concatenating:",dict4)