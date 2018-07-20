# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 05:06:23 2018

@author: Colton
"""


low = 0
high = 100
ans = (high+low)/2

count = 0

print("Please think of a number between 0 and 100.")#ask for input
print("")#\Skip a line
print("")#/Skip a line
print("Enter 'h' to indicate the guess is too high.") #\
print("Enter 'l' to indicate the guess is too low.")   #- parameters
print("Enter 'c' to indicate I guessed correctly.")   #/

print('')#skips line
str(input("Is your secret number 50?"))#asks question
working = True
while working: #run until the user input equals the computer's answer/guess
    if 'h':
        high = ans
        ans = (ans+low)/2
        str(input("Is your secret number " + str(ans) + "?"))
        count += 1
    elif 'l':
        low = ans
        ans = (high+ans)/2
        str(input("Is your secret number " + str(ans) + "?"))
        count += 1
    elif 'c':
        False
        print("Game Over")
        print("It took me" + str(count) + " tries to guess your number.")
        print("Your secret number was " + str(ans))
    else: 
        input("Invalid input. Please input either 'h', 'l', or 'c': ")


