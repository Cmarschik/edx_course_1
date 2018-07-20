# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 03:29:39 2018

@author: Colton
"""

def foo(x, y = 5):
   def bar(x):
      return x + 1
   return bar(y * 2)
          
print(foo(3, 0))


#recursive function scope example
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
        
print(fact(5))