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
while j < len(s): #while j is within lenght of string
    if s[i] <= s[j]:  #compare adjacent letters
        longS = longS + s[j]  #if right is greater, increase string length
        i += 1
        j += 1
        if j <= len(s) and (len(longS) > len(curLongS)):
            curLongS = longS #special case where j goes to end of string
            
    else:
        if (len(longS) > len(curLongS)):
            curLongS = longS
        longS = s[j]
        i +=1
        j +=1
print('Longest substring in alphabetical order is: ' + curLongS)