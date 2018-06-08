# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 03:40:07 2018

@author: brown

This program returns the remaining balance on a credit card debt
"""

balance=42
annualInterestRate=0.2
monthlyPaymentRate=0.04


    

def bal(balance, annualInterestRate, monthlyPaymentRate):
    '''
    balance: the initial balance
    annualInterestRate: pre-determined rate
    monthlyPaymentRate : percentage of balance paid monthly
    
    return: balance left round to two places
    
    '''
    for i in range(12):
            paidBalance = monthlyPaymentRate * balance
            balance = balance - paidBalance
            balance=balance + (annualInterestRate/12) * balance
    return round(balance, 2)
    

    
    
    
    
    

print('Remaining Balance: ' + str(bal(balance, annualInterestRate, monthlyPaymentRate)))