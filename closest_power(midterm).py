# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 22:19:10 2018

@author: brown
"""

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    smallestDifference = num
    maxRange = num//base
    for exp in range(int(maxRange)):
        diff = (base**exp) - num
        #print('diff ',diff)
        if abs(diff) < smallestDifference:
            smallestDifference = abs(diff)
           # print('smalldiff ',smallestDifference)
            ans = exp
           # print('ans ',ans)
   
    return ans

print(closest_power(10,550.0))