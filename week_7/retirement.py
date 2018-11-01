# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 19:39:18 2018

@author: Colton
"""
import pylab as plt

def retire(monthly, rate, terms):
    savings = [0] #y labels
    base = [0] #x labels
    mRate = rate/12
    for i in range(terms):
        base += [i] #adds in the next label for the x axis
        savings += [savings[-1]*(1+mRate) + monthly]
        # ^ the most recent savings total * new mRate(times 1) + monthly contribution
    return base, savings

def displayRetireWMonthlies(monthlies, rate, terms):
    plt.figure('retireMonth')
    plt.clf()
    for monthly in monthlies:
        xvals, yvals = retire(monthly, rate, terms) #returns 'base' & 'savings' = xvalues & yvalues
        plt.plot(xvals, yvals, label = 'retire: $' + str(monthly))
        plt.legend(loc = 'upper left')
        
displayRetireWMonthlies([500, 600, 700, 800, 900, 1000, 1100], 0.05, 40*12)
#^ includes a list of different possible amounts to set asside each month('monthlies')

def displayRetireWRates(month, rates, terms):
    plt.figure('retireRates')
    plt.clf()
    for rate in rates:
        xvals, yvals = retire(month, rate, terms)
        plt.plot(xvals, yvals, label = 'retire: $' + str(month) + ': ' + str(int(rate*100)) + '%')
        plt.legend(loc = 'upper left')
        
displayRetireWRates(800,[.03, .05, .07], 40*12)
        


def displayRetireWMonthsAndRates(monthlies, rates, terms):
    plt.figure('retireBoth')
    plt.clf()
    plt.xlim(30*12, 40*12)
    for monthly in monthlies:
        for rate in rates:
            xvals, yvals = retire(monthly, rate, terms)
            plt.plot(xvals, yvals, label = 'retire: $' + str(monthly) + ': ' + str(int(rate*100)) + '%')
            plt.legend(loc = 'upper left')
            
displayRetireWMonthsAndRates([500, 700, 900, 1100], [.03, .05, .07], 40*12)
        


def displayRetireWMonthsAndRates(monthlies, rates, terms): #easier way to view this data
    plt.figure('retireBoth')
    plt.clf() #clearsout the old'displayRetireWMonthsAndRates'
    plt.xlim(30*12, 40*12)
    monthLabels = ['r', 'b', 'g', 'k']
    rateLabels = ['-', 'o', '--']
    for i in range (len(monthlies)):
        monthly = monthlies[i]
        monthLabel = monthLabels[i%len(monthLabels)]
        for j in range (len(rates)):
            rate = rates[j]
            rateLabel = rateLabels[j%len(rateLabels)]
            xvals, yvals = retire(monthly, rate, terms)
            plt.plot(xvals, yvals, monthLabel + rateLabel, label = 'retire: $' + str(monthly) + ': ' + str(int(rate*100)) + '%')
            plt.legend(loc = 'upper left')
            
displayRetireWMonthsAndRates([500, 700, 900, 1100], [.03, .05, .07], 40*12)

