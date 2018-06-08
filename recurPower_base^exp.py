# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 09:26:37 2018

@author: brown
"""

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp==0:
        return 1
    else:
        return base*recurPower(base, exp-1)
print((recurPower(2, 4)))
