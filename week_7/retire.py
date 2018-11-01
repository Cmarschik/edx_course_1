# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 19:39:18 2018

@author: Colton
"""

def retire(monthly, rate, terms):
    savings = [0]
    base = [0]
    mRate = rate/12
    for i in range(terms):
        base += 1
        savings += [savings[-1]*(1+mRate) + monthly]
    return base, savings