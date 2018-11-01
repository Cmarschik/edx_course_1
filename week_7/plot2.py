# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 16:49:09 2018

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
    
plt.figure('lin')
plt.clf()
plt.ylim(0,1000)#creates a maximum y
plt.plot(mySamples, myLinear)
plt.figure('quad')
plt.clf()
plt.ylim(0,1000)
plt.plot(mySamples, myQuadratic)
plt.figure('lin')
plt.title('Linear')
plt.figure('quad')
plt.title('Quadratic')


plt.figure('lin quad')
plt.clf()
plt.subplot(211) #creates a seperate subplot for the following plt.plot below
plt.ylim(0,900) #subplot has its own parameters
plt.plot(mySamples, myLinear, 'b-', label = 'linear', linewidth = 2.0) #b- is blue line('-' is optional)
plt.subplot(212)
plt.ylim(0,900)
plt.plot(mySamples, myQuadratic, 'r-' , label = 'quadratic', linewidth = 3.0) #ro is red dots/circles
plt.legend(loc = 'upper left')  #creates a legend of the labels
plt.title('Linear vs. Quadratic')


'''
loc(location) can be 
        best
        upper right
        upper left
        lower left
        lower right
        right
        center left
        center right
        lower center
        upper center
        center
'''

#plt.plot(x-axis, y-axis, line color & shape, label for legend, line width) 
#only order of 1st two matter as far as I can tell

plt.figure('cube expo')
plt.clf() 
plt.subplot(121) # number of rows, number of columbs, which location to use
plt.ylim(0,140000) #different y limits
plt.plot(mySamples, myCubic, 'g^', label = 'cubic', linewidth = 4.0) #g^ is green triangles
plt.subplot(122)
plt.ylim(0,140000) #different y limits
plt.plot(mySamples, myExponential, 'r--', label = 'exponential', linewidth = 5.0) #r-- is red dashes
plt.legend() #no argument defaults to 'best' option for legend determined by pylab
plt.title('Cubic vs. Exponential')
