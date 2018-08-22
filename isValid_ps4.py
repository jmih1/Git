# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 18:28:30 2018

@author: brown
"""
from ps4a import *

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    
    """
    isValid = False
    newHand = hand.copy()
    if word in wordList:
        for char in word:
            if (char in newHand) and (newHand[char] >=1):
                isValid = True
               # newHand[char]-=1
            else:
                isValid = False
                break
   
    return isValid

print(isValidWord('hammer', {'m': 2, 'e': 1, 'h': 1, 'r': 1, 'a': 1}, wordList))
            