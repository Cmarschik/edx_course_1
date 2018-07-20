# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 16:45:49 2018

@author: Colton
"""

import math



'''
monthly_interest_rate = annualInterestRate/12 #annual is pre-defined
minimum_monthly_payment = monthlyPaymentRate*previous_balance#monthlyPR is pre-defined
monthly_unpaid_balance = previous_balance - minimum_monthly_payment
updated_balance_each_month = monthly_unpaid_balance + (MonthINtRate * Month Unpaid Balance)
'''

month = 1
balance = 42
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12.0
monthlyPaymentRate = 0.04
minimumPayment = monthlyPaymentRate * balance
monthlyUnpaidBalance = balance - minimumPayment

while month <13:
    balance = balance - (minimumPayment) + ((balance - (balance * monthlyPaymentRate)) * (monthlyInterestRate))
    print("Balance for month " + str(month) + " is " + str(round(balance, 2)))
    month += 1
    