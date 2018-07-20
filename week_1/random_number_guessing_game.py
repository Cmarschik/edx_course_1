# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 10:34:49 2018

@author: Colton
"""

#imports random stuff
import random

#setting a counter to keep score
counter = 0

#choosing random integer for the game
r = random.randint(0,100)

#intro for player pleasure
print('')
print("Try to enter numbers to total my random value between 0 & 100 without going over.")

#adds 1 to the counter for your initial guess
counter += 1

#what really matters
n = int(input("Enter a number - "))
while n < r:
    if n != r:
        counter += 1 #adds 1 to the counter for every guess
    n = int(input("Guess Another - ")) + n
if n == r:
    print("")
    print("You did it!")
    print('It took you ' + str(counter) + ' tries to guess the number.')  
else:    
    print("You lose.")

#final words for player pleasure
print('')  
print('Press "f5" to play again.')
