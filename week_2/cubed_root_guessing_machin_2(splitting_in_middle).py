# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 02:59:11 2018

@author: Colton
"""

x = int(input("Enter a number between 1 and 1 billion: "))
epsilon = 0.01
num_guesses = 0
low = 0.0
high = x
ans = (high + low)/2.0


while abs(ans**3 - x) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    num_guesses += 1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (high+low)/2.0
    print('num_guesses = ' + str(num_guesses))
    print(str(ans) + ' is close to cubed root of ' + str(x)) 