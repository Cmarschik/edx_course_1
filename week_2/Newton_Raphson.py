# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 07:31:27 2018

@author: Colton
"""

epsilon = 0.01
y = 12
guess = y/2.0
numGuesses = 0

while abs(guess*guess - y) >= epsilon:
    numGuesses += 1 
    guess = guess - (((guess*2) - y)/(2*guess)

print("Number of guesses: " + str(numGuesses))
print("Square root of " + str(y) + "is about " + str(guess) + ".")