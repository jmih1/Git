# -*- coding: utf-8 -*-
"""
Created on Wed May 16 16:32:06 2018

@author: brown
"""
s = 'abcdefghijklmnopqrstuvwxyz'
longS=s[0]
curLongS = s[0]

i=0
j=1
while j < len(s): #while 
    if s[i] <= s[j]: 
        longS = longS + s[j]
        i += 1
        j += 1
        if j <= len(s) and (len(longS) > len(curLongS)):
            curLongS = longS
            
    else:
        if (len(longS) > len(curLongS)):
            curLongS = longS
        longS = s[j]
        i +=1
        j +=1
print('Longest substring in alphabetical order is: ' + curLongS)