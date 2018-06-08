# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 11:27:01 2018

@author: brown
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup
    '''
    newTup = ()
    for t in range(len(aTup)):
        if t%2==0:
            newTup = newTup + (aTup[t],)
    return newTup

print(oddTuples((5, 1, 13, 1, 15)))