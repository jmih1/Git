# -*- coding: utf-8 -*-
"""
Created on Tue May 29 02:42:08 2018

@author: brown
"""
print('Please think of a number between 0 and 100! ')

low = 0
high = 100
ans = (high + low)//2


print('Is your secret number ' + str(ans))
response = input("Enter 'h' to indicate the guess is too high. Enter 'l' " +
      "to indicate the guess is too low. Enter 'c' to indicate " +
      "I guessed correctly : ")
while response != 'c':
    if response == 'h':
        high = ans
        ans = (high + low)//2
    elif response == 'l':
        low = ans
        ans = (high + low)//2
        #response=input('Is your secret number ' + str(ans))
    else:
        print("Your input was invalid")
        #response=input('Is your secret number ' + str(ans))
    
    print('Is your secret number ' + str(ans))
    response = input("Enter 'h' to indicate the guess is too high. Enter 'l' " +
      "to indicate the guess is too low. Enter 'c' to indicate " +
      "I guessed correctly : ")
print('Game Over. Your secret number was: ' + str(ans))




