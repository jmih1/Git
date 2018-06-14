# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 12:04:58 2018

@author: brown
"""

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    mutableString = secretWord
    for l in secretWord:
        if l not in lettersGuessed:
            mutableString = mutableString.replace(l, "_ ")
    return mutableString

 
print(getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's']))