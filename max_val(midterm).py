# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 23:49:41 2018

@author: brown
"""

def max_val(t): 
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t
    """ 
    tupMax = 0
    intMax = 0
    listMax = 0
    for l in t:
        if type(l)==tuple:
            if max(l) > tupMax:
                tupMax = max(l)
                if type(tupMax) == tuple:
                    tupMax = max(tupMax)
                elif type(tupMax) == list:
                    listMax = max(tupMax)
                    if max(l) == tuple:
                        tupMax =max(tupMax)
        elif type(l)==list:
            listMax = max(l)
            if type(listMax)==list:
                listMax = max(listMax)
            elif type(listMax)==tuple:
                tupMax = max(listMax)
                if type(listMax)==list:
                    listMax=max(listMax)
        elif type(l)==int:
             if l > intMax:
                 intMax = l
    L = [intMax, tupMax, listMax]
    #final = max[intMax, tupMax, listMax]  doesn't work, why?
            
    return max(L)


print(max_val((5, (1,2), [[1],[2]])))
    