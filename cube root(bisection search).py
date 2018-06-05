# -*- coding: utf-8 -*-
"""
Created on Tue May 29 02:11:41 2018

@author: brown
"""
cube = 8
epsilon = 0.01
numGuesses = 0
low = 0.0
high = cube
ans = (high + low)/2.0

while abs(ans**3 - cube) >= epsilon:
    numGuesses += 1
    if cube > 0:
        if ans**3 < cube:
            low = ans
        else:
            high = ans
    else:
        if ans**3 > cube:
            low = ans
        else:
            high = ans
    
    ans = (high + low)/2.0
    
print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to the cube root of ' +str(cube))
    
 
