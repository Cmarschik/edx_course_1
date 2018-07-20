# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 20:41:53 2018

@author: Colton
"""

balance = 320000
annualInterestRate = 0.2

initBalance = balance
monthlyInterestRate = annualInterestRate / 12
lower = initBalance/12
upper = initBalance * (10 + monthlyInterestRate**12)/12.0
epsilon = 0.01

while abs(balance) > epsilon:
    monthlyPaymentRate = (upper + lower)/2
    balance = initBalance
    for i in range(12):
        balance = balance - monthlyPaymentRate + ((balance - monthlyPaymentRate) * monthlyInterestRate)
    if balance > epsilon:
        lower = monthlyPaymentRate
    elif balance < -epsilon:
        upper = monthlyPaymentRate
    else:
        break
print('Lowest Payment: ', round(monthlyPaymentRate, 2))
