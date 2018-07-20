# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 05:30:13 2018

@author: Colton
"""


def fib(x):
    '''
    assumes x is an int > 0 
    returns fibonacci of x
    '''
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
