# -*- coding: utf-8 -*-
"""
Created on Tue May 29 02:02:16 2018

@author: brown

@Description: This computes the number close to the square root of 
an integer
"""

numberIn =int(input("Enter an integer whose square root you want to compute: "))
epsilon = 0.01
numGuesses = 0
low =0.0
high = numberIn
ans = (high + low)/2.0

while abs(ans**2 - numberIn) >= epsilon:
    print('low = ' + str(low) + ' high = ' +str(high) + ' ans = ' +str(ans))
    numGuesses += 1
    if ans**2 < numberIn:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
    
print('numGuesses = ' +str(numGuesses))

print(str(ans) + ' is close to the square root of ' + str(numberIn))