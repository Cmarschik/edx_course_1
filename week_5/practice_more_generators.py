# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 15:05:06 2018

@author: Colton
"""

def genPrimes():
    primeList = []   # primes generated so far
    recentNum = 1      # most recent number tried
    while True:
        recentNum += 1
        for p in primeList:
            if recentNum % p == 0:
                break
        else:
            primeList.append(recentNum)
            yield recentNum