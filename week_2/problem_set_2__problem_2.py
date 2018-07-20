# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 17:03:17 2018

@author: Colton
"""

balance = 3329
initBalance = balance
monthlyPaymentRate = 0
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12

while balance>0:
    for i in range(12):
        balance = balance - monthlyPaymentRate + ((balance - monthlyPaymentRate) * monthlyInterestRate)
    if balance > 0:
        monthlyPaymentRate += 10
        balance = initBalance
    elif balance <= 0:
        break
    
print("Lowest payment: " + str(balance/12))