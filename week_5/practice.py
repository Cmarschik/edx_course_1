# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 17:41:34 2018

@author: Colton


class fraction(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
    def __str__(self):
        return str(self.numer) + '/' + str(self.denom)
    def getNumer(self): #called a 'getter'
        return(self.numer)
    def getDenom(self):
        return(self.denom) #called a 'getter'
    def __add__(self, other): #how fractins are added
        numerNew = other.getDenom() * self.getNumer() + other.getNumer() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return fraction(numerNew, denomNew)
    def __sub__(self, other): #how fractions are subtracted
        numerNew = other.getDenom() * self.getNumer() - other.getNumer() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return fraction(numerNew, denomNew)    
    def convert(self): #converts to float
        return self.getNumer() / self.getDenom()
    
    
oneHalf = fraction(1,2)
twoThirds = fraction(2,3)
threeQuarters = fraction(3,4)
new = oneHalf + twoThirds
secondNew = twoThirds - threeQuarters

print(oneHalf)
print(twoThirds)
print(threeQuarters, '\n')
print(new)
print(new.convert())
print(secondNew)
print(secondNew.convert(), '\n')
print(oneHalf.getNumer()) #gets numerator from 1/2
print(twoThirds.getDenom()) #gets denominator from 2/3
"""




class intSet(object):
    def __init__(self):
        self.vals = []
    def insert(self,e):
        if not e in self.vals: #adds digit to the list if it's not in there
            self.vals.append(e) #adds nothing/skips over if e is in list
    def member(self,e):
        return e in self.vals #returns True/False depending if digit is in list
    def remove(self,e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e), 'not found')
    def __str__(self):
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return '{' + result[:-1] + '}'
    
s = intSet()
print(s)
s.insert(3)
s.insert(4)
s.insert(3) #only one 3 is printed bc
print(s)
print(s.member(3))
print(s.member(4))
print(s.member(6), '\n')
s.remove(3)
s.insert(5)
print(s) #now has 4 and 5
#s.remove(7) #this prints the error that I set up in "remove-except" above b/c there is no 7

    
    
    
    
    
    