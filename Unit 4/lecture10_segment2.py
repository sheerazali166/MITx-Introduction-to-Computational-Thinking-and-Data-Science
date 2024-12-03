#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 10:05:05 2024

@author: sheeraz
"""

import random, pylab, numpy

# set line width
pylab.rcParams["lines.linewidth"] = 4

# set font size for titles
pylab.rcParams["axes.titlesize"] = 20

# set font size for labels on axes
pylab.rcParams["axes.labelsize"] = 20

# set size of numbers on x-axis
pylab.rcParams["xtick.labelsize"] = 16

# set size of numbers on y-axis
pylab.rcParams["ytick.labelsize"] = 16

# set size of ticks on x-axis
pylab.rcParams["xtick.major.size"] = 7

# set size of ticks on y-axis
pylab.rcParams["ytick.major.size"]  = 7

pylab.rcParams["lines.markersize"] = 10

# set number of examples shown in legends
pylab.rcParams["legend.numpoints"] = 1


def getData(fileName):
    
    dataFile = open(fileName, "r")
    
    distances = []
    
    masses = []
    
    dataFile.readline()  #  discard header
    
    for line in dataFile:
        
        d, m = line.split()
        
        distances.append(float(d))
        
        masses.append(float(m))
        
    dataFile.close()

    return (masses, distances)



def labelPlot():
    
    pylab.title("Measure displacement of Spring")
    pylab.xlabel("|Force| Newtons")
    pylab.ylabel("Distance (meters)")
    
    

def plotData(fileName):

    xVals, yVals = getData(fileName)
    
    xVals = pylab.array(xVals)
    
    yVals = pylab.array(yVals)
    
    xVals = xVals * 9.81 #acc. due to gravity
    
    pylab.plot(xVals, yVals, "bo", label = "Measured displacements")
    
    labelPlot()
    
    
    
def fitData(fileName):

    xVals, yVals = getData(fileName)

    xVals = pylab.array(xVals)
    
    yVals = pylab.array(yVals)
    
    xVals = xVals * 9.81 # get force
    
    pylab.plot(xVals, yVals, "bo", label = "Measured points")
    
    a, b = pylab.polyfit(xVals, yVals, 1)
    
    estYVals = a * xVals + b
    
    print("a =", a, "b =", b)
    
    pylab.plot(xVals, estYVals, "r", label = "Linear fit,  = " +
                   str(round(1 / a, 5)))
    
    
    pylab.legend(loc = "best")
    
    pylab.show()
    

fitData("springData.txt")
    

def fitData1(fileName):
    
    xVals, yVals = getData(fileName)
    
    xVals = pylab.array(xVals)
    
    yVals = pylab.array(yVals)
    
    xVals = xVals * 9.81 # get force 
    
    pylab.plot(xVals, yVals, "bo", label = "Measure points")
    
    labelPlot()
    
    model = pylab.polyfit(xVals, yVals, 1)
    
    estYVals = pylab.polyval(model, xVals)
    
    pylab.plot(xVals, estYVals, "r", label = "Linear fit  = " +
                   str(round(1 / model[0], 5)))
    
    
    pylab.legend(loc = "best")
    
    pylab.show()
    
    
# fitData1("springData.txt")

def genParabolicData(a, b, c, xVals, fracOutliers):

    yVals = []

    for x in xVals:
        
        theoreticalVals = a * x**2 + b*x  + c
        
        if random.random() > fracOutliers:
            
            yVals.append(theoreticalVals + random.gauss(0, 1000))

        else:
            
            # generate outlier
            yVals.append(theoreticalVals + random.gauss(0, theoreticalVals * 2))
            
    return yVals


# parameters for generating data 
xVals = range(50, 51, 1)

a, b, c = 3.0, 0.0, 0.0

fracOutliers = 0.0

# generate data
random.seed(0)

yVals = genParabolicData(a, b, c, xVals, fracOutliers)

pylab.plot(xVals, yVals, "o", label = "Data Points")

# pylab.title("Mystery Data")



# Try linear model

model1 = pylab.polyfit(xVals, yVals, 1)

pylab.plot(xVals, pylab.polyval(model1, xVals), label = "Linear Model")


# Try Quadratic Model
model2 = pylab.polyfit(xVals, yVals, 2)

pylab.plot(xVals, pylab.polyval(model2, xVals), "r--",
               label = "Quadratic Model")


pylab.legend()


pylab.show()


   