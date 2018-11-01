# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 16:18:45 2018

@author: Colton
"""

import pylab as plt
#allows me to referance any 'pylab" procedure as...
#plt.<procName>

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range (0,30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)#usually use '2'
    

'''
assumes lists are of the same length
assumes 'mySample' is X-value
assumes any other list I chose is Y-value
'''

plt.figure('lin') #names a figure for the line below
plt.xlabel('sample points') #labels the x-axis
plt.ylabel('linear function') #labels the y-axis
plt.plot(mySamples, myLinear) #mySamples are X-values and I chose myLinear as Y-values
plt.figure('quad')
plt.xlabel('sample points')
plt.ylabel('quadratic function')
plt.plot(mySamples, myQuadratic)
plt.figure('cube')
plt.xlabel('sample points')
plt.ylabel('cubic function')
plt.plot(mySamples, myCubic)
plt.figure('expo')
plt.plot(mySamples, myExponential)
plt.figure('expo')#reopens exponential and adds labels
plt.xlabel('sample points')
plt.ylabel('exponential function')


plt.figure('lin') #reopens the figures
plt.clf()#clears any previous version of this figure / no x or y label in this case
plt.title('Linear')
plt.figure('quad') 
plt.clf() #this no longer has the x or y label
plt.title('Quadratic')
plt.figure('cube') 
plt.title('Cubic')
plt.figure('expo')
plt.title('Exponential')
