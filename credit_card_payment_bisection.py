# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 10:25:58 2018

@author: brown
"""

def creditCardBisec(balance, annualInterestRate):
    '''
    balance : Original balance to be paid off
    annualInterestRate : Interest rate on credit
    
    return : fixed amount to pay off all the balance
    
    '''
    downbound = balance/12.0
    global monthlyInterestRate 
    monthlyInterestRate = annualInterestRate/12
    uppbound = (balance * (1 + monthlyInterestRate) **12)/12.0
    payment = (uppbound + downbound)/2.0
    origbalance = balance 
   
    while check(origbalance, payment) != 0:
        origbalance = balance
        check(origbalance, payment)
        if  check(origbalance, payment) > 0:
            downbound = payment
        else:
            uppbound = payment
        payment = (uppbound + downbound)/2
        
    
    return round(payment,2)

def check(origbalance, payment):
    for i in range(12):
        origbalance -= payment
        origbalance = origbalance + (monthlyInterestRate * origbalance)
    return round(origbalance,2)

    
print('Lowest Payment: ',creditCardBisec(balance, annualInterestRate))