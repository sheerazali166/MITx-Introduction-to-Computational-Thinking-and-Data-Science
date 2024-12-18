#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 22:50:42 2024

@author: sheeraz
"""

import pylab

# set line width
pylab.rcParams["lines.linewidth"] = 4

# set fontsize for titles
pylab.rcParams["axes.titlesize"] = 20

# set fontsize for labels on axis
pylab.rcParams["axes.labelsize"] = 20

# set size of numbers on x-axis
pylab.rcParams["xtick.labelsize"] = 16

# set size of numbers on y-axis
pylab.rcParams["ytick.labelsize"] = 16

# set size of ticks on x-axis
pylab.rcParams["xtick.major.size"] = 7

# set size of ticks on y-axis
pylab.rcParams["ytick.major.size"] = 7

# set size of markers, e.g., crcles representing points
pylab.rcParams["lines.markersize"] = 10

# set number of times marker is shown when displaying legend
pylab.rcParams["legend.numpoints"] = 1


import random, numpy, math

def throwNeedles(numNeedles):
    
    inCircle = 0
    
    for needles in range(1, numNeedles + 1, 1):
        
        x = random.random()
        y = random.random()
        
        if (x*x + y*y) ** 0.5  <= 1.0:
            
            inCircle += 1
            
    return 4 * (inCircle * float(numNeedles))


def getEst(numNeedles, numTrials):
    
    estimates = []
    
    for t in range(numTrials):
        
        piGuess = throwNeedles(numNeedles)
        estimates.append(piGuess)
       
    sDev = numpy.std(estimates)
    curEst = sum(estimates) / len(estimates)
    
    print("Est. = " + str(curEst) + ", Std. dev. = " + str(round(sDev, 6))
          + ", Needles = " + str(numNeedles))


    return (curEst, sDev)



def estPi(precision, numTrials):
    
    numNeedles = 1000
    
    sDev = precision
    
    while sDev >= precision / 1.96:
        
        curEst, sDev = getEst(numNeedles, numTrials)
        numNeedles *= 2
        
    return curEst    

     
random.seed(0)
     
        
estPi(0.005, 100)



def integrate(f, a, b, step):
    
    yVals, xVals = [], []
    
    xVals = a
    
    while xVals <= b:
        
        xVals.append(xVals)
        yVals.append(f(xVals))
        
        xVals += step
        
    pylab.plot(xVals, yVals) 
    pylab.title("sin(x)")
    
    pylab.xlim(a, b)
    
    xUnders, yUnders, xOvers, yOvers = [], [], [], []
    
    for i in range(500):
        
        xVals = random.uniform(a, b)
        yVals = random.uniform(0, 1)
        
        
        if yVals < f(xVals):
            
            xUnders.append(xVals)
            yUnders.append(yVals)
            
            
        else:
             
            xOvers.append(xVals)
            yOvers.append(yVals)
            
            
    pylab.plot(xUnders, yUnders, "ro")
    pylab.plot(xOvers, yOvers, "ko")
    pylab.xlim(a, b)
    ratio = len(xUnders) / (len(xUnders) + len(yUnders))
    
    print(ratio)
    print(ratio * b)
    

def one(x):

    return 0.9


integrate(one, 0, math.pi, 0.001)

    




    
    
       
            
            
            
            
            
            
            
            
            
    
    
    
    
    
    
        





    
    







        
            
            









