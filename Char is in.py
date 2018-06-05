# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 14:09:17 2018

@author: brown

code referenced from Ying_yu on Edx posts
"""
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    
    '''
    if len(aStr) == 0:
       return False
    elif len(aStr) == 1:
       return char == aStr
    else:
       mid = len(aStr)//2
       if char == aStr[mid]:
           return True
       elif char < aStr[mid]:
           return isIn(char, aStr[:mid])
       else:
           return isIn(char, aStr[mid+1:]) 
       
print(isIn('w', 'ccdefhkkmoqqqtuuwwwz'))