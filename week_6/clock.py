# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 14:27:32 2018

@author: Colton
"""
import time

def c_to_f(c):
    return c*9/5 +32

time0 = time.clock()#time rn before calculation
ans1 = c_to_f(100) #run this at 100 celsius 
time1 = time.clock() - time0 #time rn after calculation ran

print(ans1)
print(time1)



def cube(x):
    return x * x * x

time2 = time.clock()
ans2 = cube(9999999**99)
time3 = time.clock() - time2

print(ans2)
print(str(time3))

print(' ')

n = 10
def g(n): #quadratic
    x = 0
    for i in range(n):
        for j in range(n): 
            x+=1
    return x

print(g(n))
            