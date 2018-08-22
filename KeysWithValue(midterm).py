# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 23:29:38 2018

@author: brown
"""

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    List = []
    keys = aDict.keys()
    for key in keys:
        if aDict[key] == target:
            List.append(key)
    return sorted(List)

aDict = {'Ana':'B', 'John':4, 'Denise':'4', 'Katy':'A'}


print(keysWithValue(aDict, 4))