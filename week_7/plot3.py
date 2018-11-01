# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 18:05:13 2018

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





plt.figure('cube expo lin')
plt.clf() 
plt.plot(mySamples, myCubic, 'g^', label = 'cubic', linewidth = 4.0) #g^ is green triangles
plt.plot(mySamples, myExponential, 'r--', label = 'exponential', linewidth = 5.0) #r-- is red dashes
plt.yscale('log') #plots the y axis on a log scale / each y increases by an order of magnitude
plt.legend() #no argument defaults to 'best' option for legend determined by pylab
plt.title('Cubic vs. Exponential')

plt.figure('cube expo log')
plt.clf() 
plt.plot(mySamples, myCubic, 'g^', label = 'cubic', linewidth = 4.0) #g^ is green triangles
plt.plot(mySamples, myExponential, 'r--', label = 'exponential', linewidth = 5.0) #r-- is red dashes
plt.legend() #no argument defaults to 'best' option for legend determined by pylab
plt.title('Cubic vs. Exponential')