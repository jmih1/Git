# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 12:32:48 2018

@author: brown
"""

import string

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    newString = string.ascii_lowercase
    for l in lettersGuessed:
        newString = newString.replace(l, "")
        
    return newString

print(getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's']))