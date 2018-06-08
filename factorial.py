# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 08:51:06 2018

@author: brown
"""

def fact(n):
    '''
    n : number input
    
    return : factorial of number
    '''
    if n==1:
        return 1
    else:
        return n*fact(n-1)

print(fact(4))