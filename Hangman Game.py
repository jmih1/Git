# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


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

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("************************************************************")
    wordLength = len(secretWord)
    guesses = 8
    lettersGuessed = [] 
    getAvailableLetters(lettersGuessed)
    mistakesMade = 0
   
    
    print("Welcome to the hangman Game. Please Don't hang me!")
    print("I am a " + str(wordLength) + "-letter Word")
    print("*****************************************")
    print(secretWord)
    while guesses > 0:
        print("Status of guessed word: " + getGuessedWord(secretWord, lettersGuessed))
        print("You have " + str(guesses) + " guesses left")
        print("The available words to choose from are " + getAvailableLetters(lettersGuessed))
        guess = input("Select from available letters: ")
        while guess.lower() not in getAvailableLetters(lettersGuessed):
            print("Your selection was not in the available letters")
            guess = input("Select from available letters: ")
        lettersGuessed.append(guess.lower())
        if guess.lower() in secretWord:
            print("Good Guess: " + getGuessedWord(secretWord, lettersGuessed))
            getAvailableLetters(lettersGuessed)
            if isWordGuessed(secretWord, lettersGuessed):
                print("You won")
                break
        else:
            print("Wrong guess: " +  getGuessedWord(secretWord, lettersGuessed))
            guesses -= 1
            mistakesMade += 1
            print("Sorry, that letter is not in the secret word")
            getAvailableLetters(lettersGuessed)
            print("*****************************************")
      
    if not (isWordGuessed(secretWord, lettersGuessed)):
        print("I got hanged")
        print("Better Luck Next Time")
    return None
    
    






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
