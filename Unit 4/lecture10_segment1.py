#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 08:22:35 2024

@author: sheeraz
"""

import random, pylab, numpy

# set line width
pylab.rcParams["lines.linewidth"] = 4

# set font size for titles
pylab.rcParams["axes.titlesize"] = 20

# set font size for labels on axis
pylab.rcParams["axes.labelsize"] = 20

# set size of numbers on axis
pylab.rcParams["xtick.labelsize"] = 16

# set size of numbers on y-axis
pylab.rcParams["ytick.labelsize"] = 16

# set size of ticks on x-axis
pylab.rcParams["xtick.major.size"] = 7

# set size of ticks on y-axis
pylab.rcParams["ytick.major.size"] = 7

# set size of markers
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
    
    pylab.title("Measured Displacement of Spring")
    pylab.xlabel("|Force| (Newtons)")
    pylab.ylabel("Distance (meters)")
    
    
def plotData(fileName):
    
    xVals, yVals = getData(fileName)
    
    xVals = pylab.array(xVals)
    
    yVals = pylab.array(yVals)
    
    xVals = xVals * 9.81  #  acc due to gravity
    
    pylab.plot(xVals, yVals, "bo", label = "Measured displacement")
    
    
    labelPlot()
    
    pylab.show()
    
    
plotData("springData.txt")




