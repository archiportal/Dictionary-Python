# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 12:33:53 2020

@author: ARCHISMAN ROY
"""

dictionary = {'a':7, 'b':10, 'c': 9}
print(dictionary)

kmax = max(dictionary.keys(), key=(lambda k: dictionary[k]))
kmin = min(dictionary.keys(), key=(lambda k: dictionary[k]))

print('Maximum Value: ',dictionary[kmax])
print('Minimum Value: ',dictionary[kmin])