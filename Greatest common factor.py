# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 08:19:55 2018

@author: brown
"""

def gcdIter(a, b):
    '''
    a,b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    ans=0
    if a > b :
        test=b
        while test>=1:
            if b%test==0 and a%test==0:
                ans=test
                break
            else:
                ans=test
                test -=1
    else:
        test=a
        while test>=1:
            if b%test==0 and a%test==0:
                ans=test
                break
            else:
                test -=1
                ans=a
    
    return ans      

print((gcdIter(91,105)))