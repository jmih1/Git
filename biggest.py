# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 09:11:03 2018

@author: brown
"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    lenOfVals = [] #create an array of lengths of values
    for val in aDict.values():
        lenOfVals.append(len(val)) #get an array of lengths of values
    
    largest = max(lenOfVals) #find the max length
    
    
    for key in aDict.keys():
        if len(aDict[key]) == largest: #compare largest and length 
            return key
        elif largest == 0:
            return None
        
animals = { 'a': ['aardvark', 'brr', 'brr', 'b' ], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
print(animals)
print(biggest(animals))
