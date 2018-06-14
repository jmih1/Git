# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 20:32:39 2018

@author: brown
"""

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    test = False
    for l in secretWord:
        if l in lettersGuessed:
            test = True
        else:
            test = False
            break
    return test
        

secretWord = "apples"
lettersGuessed = ['a', 'p', 'l', 'o', 'e', 's']
print(isWordGuessed(secretWord, lettersGuessed))