# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 09:05:32 2018

@author: brown
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    ans=1
    if exp !=0:
        for i in range(exp):
            ans *=base
        
    return ans
print((iterPower(5, 0)))