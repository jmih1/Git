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
        test=b #if b is smaller, set it to test since gcd won't be greater
        while test>=1: #ensure gcd is positive and not zero
            if b%test==0 and a%test==0: #f test divides both, set it to ans
                ans=test
                break
            else:
                ans=test #else set test to ans and decrease
                test -=1
    else:
        test=a #set smaller number to gcd
        while test>=1:
            if b%test==0 and a%test==0:
                ans=test
                break
            else:
                test -=1
                ans=a
    
    return ans      

print((gcdIter(91,105)))