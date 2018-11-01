# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 13:39:28 2018

@author: Colton
"""
#coordinate is the subclass and object is the superclass
class Coordinate(object):
    def __init__ (self, x, y):
        self.x = x #value passed in for 'x' above is now bound to this x
        self.y = y #value passed in for 'y' above is now bound to this y
    def distance(self, other):
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5
    def __str__(self): #special method on what I want displayed in console
        return "<"+ str(self.x) + "," + str(self.y) + ">" #all displayed as string
    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)
    
c = Coordinate(3,4)
origin = Coordinate(0,0)
print(c.x)
print(c.y)
print(origin.x)
print(origin.y)
#print(object.method(paramater))
print(c.distance(origin))#python does 'self' automatically
#print(class.method(parameter, parameter))
print(Coordinate.distance(c, origin)) #also does distance between c and origin
print(c)
print(type(c))
#use is instance to check if object is a Coordinate = True/False
print(isinstance(c, Coordinate))#is c an instance of Coordinate
foo = c - origin
print(foo)

