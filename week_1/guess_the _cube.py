# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 13:33:31 2018

@author: Colton
"""


s = 'azcbobobegghakl'

word = 0
n = 0

for i in range(s):
    if s[n] == 'b':
        n += 1
        if s[n] == 'o':
            n += 1
            if s[n] == 'b':
                n += 1   
                word += 1
    else:
        n += 1
print(word)