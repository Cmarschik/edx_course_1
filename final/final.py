# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 12:54:21 2018

@author: Colton
"""
#INCOMPLETE FINAL

s1 = 'abcd'
s2 = 'efghi'

def laceStrings(s1, s2): #p3
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    new1 = len(s1)
    new2 = len(s2)
    s3 = ''
    while new1 > 0: 
        for i in s1:
            if s1[i]%2 == 0:
                s3 += s1[i]
    while new2 > 0:
        for i in s2:
            if s2[i]%2 == 1:
                s3 += s2[i]            
    return(s3)                    
    
laceStrings(s1, s2)




def largest_odd_times(L): #p4
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
        
    largest = 0
    recent_largest = 0
    for i in L:
        if i > largest:
            largest = i
    if L.count(largest)%2 ==1:
            print(largest)
    elif L.count(largest)%2 == 0: #all is good just gotta fix this elif section
        recent_largest = largest
        while recent_largest == largest:
            L.remove(largest)
    else:
       print(None)
       
largest_odd_times([3,3,2,0]) #returns 2        
largest_odd_times([2,2,4,4]) #returns none
largest_odd_times([3,9,5,3,5,3]) #returns 9
Test: largest_odd_times([3,0,5,3,5,3]) #returns 3



def dict_interdiff(d1, d2): #p5
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    
    
    
class USResident(Person): #p6  #works on "usresident" document 
    '''
    USResident is a subclass of "person"
    each resident has a name and whether or not they are a resident
    '''
    def __init__(self, name, status):
        """ 
        Initializes a Person object. A USResident object inherits 
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
    
        if status in ["citizen", "legal_resident", "illegal_resident"]:
            Person.__init__(self, name)
            self.status = status
        else:
            raise ValueError

        
        
    def getStatus(self):
        """
        Returns the status
        """
        return self.status
        



class Container(object): #p7
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object 
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s

class ASet(Container): #p7
    def remove(self, e):
        """assumes e is hashable
           removes e from self"""
        self.e = e
        e -= e

    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise."""
        if e in self.vals:
            return True
        else:
            return False
        
d1 = ASet()
d1.insert(4)
print(d1.is_in(4))
d1.insert(5)
print(d1.is_in(5))
d1.remove(5)
print(d1.is_in(5))

#True
#True
#False