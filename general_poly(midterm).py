# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 00:51:17 2018

@author: brown
"""


def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 
    """
    def multi(x):
        ans = 0
        k = len(L)-1
        for i in L:
            ans += i*(x**k)
            print(ans)
            k-=1
        return ans
    
    return multi
        

print(general_poly([1, 2, 3, 4])(10))           
            