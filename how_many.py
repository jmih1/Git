# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 08:51:24 2018

@author: brown
"""
'''
Cleary misunderstood the question
def how_many(aDict):
    
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    
    dictlength = len(aDict.values()) #get length of values list
    sumOfvalues = (dictlength * (dictlength +1))//2 #use formula for finding sum of first n natural numbers
    return sumOfvalues
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
print(how_many(animals))
'''

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    sumOfValues = 0
    for l in aDict.values():
        sumOfValues += len(l)
    return sumOfValues

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
print(how_many(animals))