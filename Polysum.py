# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 03:08:36 2018

@author: brown

This takes the number of sides n, and length s of a polygon 
and finds the sum of the area and square of perimeter rounded
to four places
"""

from math import * #import math module 

def polysum(n, s):
    area = (0.25 * n * s **2)/tan(pi/n)
    perimeter = n*s
    
    add = area + perimeter**2 
    
    return round(add,4) #round off number to 4 places