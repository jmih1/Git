# -*- coding: utf-8 -*-
"""
Created on Wed May 16 16:17:17 2018

@author: brown
"""

s='bobobkyoboooobobboboboohobobobovbobooboboobk'
count=0
for i in range(len(s)-2):
    if s[i:i+3]=='bob':
        count +=1
print('Number of times bob occurs is: ' +str(count))
        