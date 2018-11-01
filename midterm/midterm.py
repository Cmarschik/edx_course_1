# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 12:22:55 2018

@author: Colton
"""

"""
#Problem 3
a1 = 5
a2 = 3
b1 = 3
b2 = 8
c1 = 8
c2 = 3
x1 = 2
x2 = 3
def evalQuadratic(a, b, c, x):
   '''
   a, b, c: numerical values for the coefficients of a quadratic equation
   x: numerical value at which to evaluate the quadratic.
   '''
   return a*x*x + b*x + c

def twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    '''
    a1, b1, c1: one set of coefficients of a quadratic equation
    a2, b2, c2: another set of coefficients of a quadratic equation
    x1, x2: values at which to evaluate the quadratics
    '''
    a = evalQuadratic(a1,b1,c1,x1) 
    b = evalQuadratic(a2,b2,c2,x2)
    print(a + b)


#Problem 4
listA = [1,2,3]
listB = [4,5,6]
def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    count = 0
    total = 0
    for i in range(len(listA)):
        oneTotal = listA[0 + count] * listB[0 + count]
        count += 1
        total += oneTotal
    return(total)
 


#Problem 5 / incomplete
d = {1:10, 2:20, 3:30}#examples
#d = {1:10, 2:20, 3:30, 4:30}#examples
#d = {4:True, 2:True, 0:True}#examples

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    d1 = {}
    count = 0
    for i in range(len(d)):
        d1 += {d[1+count]:d[1+count]}
        count += 1
    return d
    print(d1)
   
   
#Problem 6 / 13.33/20 points
def gcd(a, b):
    a = 12
    b = 20
    '''
    a, b: two positive integers
    Returns the greatest common divisor of a and b
    '''
    if a > b:
        while b > 0:
            a = b
            b = a % b
        return(a)
    elif b > a:
        while a > 0:
            b = a
            a = b % a
        return(b)
"""

from collections import counter
#Problem 7 
def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    data = counter(L)
    return data.most_common(L)
run_satisfiesF(L, satisfiesF)


    