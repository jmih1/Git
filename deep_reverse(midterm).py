# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 22:42:59 2018

@author: brown
"""

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    
    '''
    i = 0
    j = len(L) - 1
    midpoint = len(L)/2
    print(midpoint)
    while (i < midpoint) and (j >= midpoint):
        temp = L[i]
        L[i] = L[j]
        L[j] = temp
        i+=1
        j-=1
  
    
        
    for l in L: #l is internal list position
        a = 0
        b = len(l) - 1
        midp = len(l)/2
        while (a < midp) and (b >=midp):
            temp = l[a]
            l[a] = l[b]
            l[b] = temp
            a+=1
            b-=1
    '''
    L.reverse()
    
    for l in L:
        l.reverse()
        
    return L

L = [[0, 1, 2], [1, 2, 3], [3, 2, 1], [10, -10, 100]]

print(deep_reverse(L))
        