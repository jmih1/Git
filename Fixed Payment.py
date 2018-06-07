# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 08:21:08 2018

@author: brown
"""

def fixed(balance, annualInterestRate):
    fix=0.01
    origbalance = balance
    while origbalance >= 0:
        origbalance = balance
        for i in range(12):
            origbalance = origbalance - fix
            origbalance = origbalance + (annualInterestRate/12) * origbalance
        fix += .01
    return fix-.01

print('Lowest Payment: ' + str(fixed(3329, 0.2)))
        


'''
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