# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 10:10:10 2018

@author: Colton
"""
'''
t = (1, "two", "three", 4)
print(t)
print(t[0])

s = (5,6)
ts = t + s
print(ts)
print(ts[1:4])
print(t[1])
print(t[1:2])

s=('hello')
ss=('hellos',)
print(s)#string
print(ss)#tuple / comma after piece
print(type(s))
print(type(ss))

(s,ss) = (ss,s) #tuples swap vaiables without temporary variables("temp")

print(s)

L = ['dog', 'happy', "potato"]

count = 0
for i in L:
    count += 1
print(count)
print(L[0:1])
print(L[0])

L.append('hippo')
print(L)


L1 = [2,1,2]
L1.extend([0,5,4,5])
del(L1[1])
L2 = [5,3,6]
L3 = L1 + L2
print(L3)
print(L2.pop())#removes piece from list(returns it) / if not specified, removes end(returns it)
print(L2)
L3.remove(2)#searches for "2" and removes the first one
print((L3))


s = 'Hello world. How are you?'
print(list(s))
print(s.split())#splits by a given parameter / no parameter implies split by spaces
print('_'.join(s))#turns a list into a string / words are sepearated by what is in quotes before the "."
print(''.join(s))


print('')
j = [9,3,2,4,6,4,3,4]

print(sorted(j))#orders string into a list of ordered characters / does NOT change j
print(j)

j.sort()#MUTATES j to be in order
print(j)

j.reverse()#MUTATES j to be in backwards order
print(j)


w = [3,4,3]
w.sort()
print(w)


warm = ['red', 'yellow', 'orange']
hot = warm#same string

print(hot)#same as warm since it's a ilst
print(warm)#same as hot since it's a list

hot.append('pink')#also appends w"warm"

print(hot)
print(warm)


cool = ['blue', 'green', 'grey']#dif string than "chill"
chill = ['blue', 'green', 'grey']#dif string than "cool"

print(cool)
print(chill)
chill[1] = 'lightBlue'
print(cool)
print(chill)


cool = ['blue', 'green', 'grey']
chill = cool[:]#this makes "chill" to be a clone of "cool"
chill.append('white')
print(cool)
print(chill)


def removeDups(L1,L2):
    L1Copy = L1[:]
    for e in L1Copy:#must make a copy or else this iteration won't work correctly as the list size changes b/c removing duplicates shortens it
        if e in L2:
            L1.remove(e)
            
L1 = [2,3,4,5,9]
L2 = [2,3,9,10,22]
removeDups(L1,L2)

print(L1)


def applyToEach(L,f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
L = [1, -2, 3.4]

applyToEach(L,abs)#find abs value
print(L)
applyToEach(L,int)#rounds down to make integers
print(L)


for elt in map(abs, [2,-4,3,-3.3]):#"map" is a general purpose function allowing to do something to a full list
    print(elt)
print(' ')
print(' ')    




L1 = [2,1,-3,-3.3]
L2 = [3,93,-34.8,-3.2]
for elt in map(min,L1,L2):#finds the minimums for each index comparitively b/w L1 and L2
    print(elt)
'''
myDict = {}#Empty dictionary named "myDict" / use CURLY BRACES to define dictionaries

grades = {'James':'A+', 'Colton':'A+', 'Vish':'A+', 'Victor':'B+', 'Sarah':'A'}#{key:value}
print(grades['James']) # use brackets for 'grades'

grades['Tony'] = 'B'#adds the name "Tony"
print(grades)

print('John' in grades)#test to see if a name is in the dictionary / False
print('Vish' in grades)#test to see if a name is in the dictionary / True

del(grades['Sarah'])#deletes 'Sarah' from the dictionary

print(grades)
print(' ')
print(' ')

print(grades.keys())#calls on the keys using a method(which requires open/close parenthesis)
print(grades.values())#calls on the values using a method(which requires open/close parenthesis)\
