# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 10:25:58 2018

@author: brown
"""

def creditCardBisec(balance, annualInterestRate):
    downbound = balance/12
    uppbound = (balance * (1 + (annualInterestRate/12))**12)
    payment = 