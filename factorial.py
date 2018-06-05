# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 08:51:06 2018

@author: brown
"""

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

print(fact(4))