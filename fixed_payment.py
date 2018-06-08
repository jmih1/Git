# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 08:21:08 2018

@author: brown
"""

def fixed(balance, annualInterestRate):
    '''
    balance : balance to be paid
    annualInterestRate : pre-determined rate
    
    return : fixed payment
    
    '''
    fix=10
    origbalance = balance #set balance to original balance to be altered
    while origbalance >= 0: #until balance is paid off
        origbalance = balance
        for i in range(12):
            origbalance = origbalance - fix #perform deduction
            #add monthly interest to balance 
            origbalance = origbalance + (annualInterestRate/12) * origbalance
        fix += 10
    return fix-10

print('Lowest Payment: ' + str(fixed(3329, 0.2)))
        


'''
Ignore the following code 

def checkPay(balance, annualInterestRate, fixedPay):
    for i in range(12):
        balance = balance - fixedPay
        balance = balance + (annualInterestRate/12)
    return balance

def fixed(balance, annualInterestRate):
    fixedPay = 10
     if checkPay(balance, annualInterestRate, fixedPay) <=0:
         return checkPay(balance, annualInterestRate, fixedPay)
     else:
         fixedPay +=10
         checkPay(balance, annualInterestRate, fixedPay)
        

    
print('Lowest Payment: ' + str(fixed(3329, 0.2)))

'''