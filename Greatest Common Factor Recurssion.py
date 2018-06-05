# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 09:07:07 2018

@author: brown
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b==0:
        return a 
    else:
        return gcdRecur(b, a%b)
        
print(gcdRecur(35, 7))