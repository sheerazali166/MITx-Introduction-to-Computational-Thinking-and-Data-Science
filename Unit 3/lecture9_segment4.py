#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 10:53:00 2024

@author: sheeraz
"""

import random, pylab, numpy

# set line width
pylab.rcParams["lines.linewidth"] = 4

# set font size for titles
pylab.rcParams["axes.titlesize"] = 20

# set font size for labels on axes
pylab.rcParams["axes.labelsize"] =  20

# set size of numbers on x-axis
pylab.rcParams["xtick.labelsize"] = 16

# set size of numbers on y-axis
pylab.rcParams["ytick.labelsize"] = 16

# set size of ticks on axis
pylab.rcParams["xtick.major.size"] =  7

# set size of ticks on y-axis
pylab.rcParams["ytick.major.size"] = 7

# set size of markers
pylab.rcParams["lines.markersize"] = 10

# set number of examples shown in legends
pylab.rcParams["legend.numpoints"] = 1


def makeHist(data, title, xlabel, ylabel, bins = 20):
    
    pylab.hist(data, bins = bins)
    pylab.tile(title)
    pylab.xlabel(xlabel)
    pylab.ylabel(ylabel)
    pylab.show()
    
    
def getHighs():
    
    inFile = open("temperatures.csv")
    
    population = []

    for l in inFile:
        
        try:
            
            tempC = float(l.split(",")[1])
            
            population.append(tempC)
            
        except:
            
            continue
        
    return population
   
    
def getMeansAndSDs(population, sample, verbose = False):
    
    popMean = sum(population) / len(population)
    
    sampleMean = sum(sample) / len(sample)
    
    if verbose:
        
        makeHist(population, "Daily High 1961-2015, Population\n"
                     + "(mean = " + str(round(popMean, 2)) + ")",
                         "Degrees C", "Number Days")
        
        pylab.figure()
        
        makeHist(sample, "Daily High 1961-2015, Sample\n" + "(mean ="
                     + str(round(sampleMean, 2)) + ")", "Degrees C",
                         "Number Days")
        
        print("Populaton mean = ", popMean)
        print("Standard deviaton of population =", numpy.std(population))
        
        print("Sample mean =", sampleMean)
        print("Standard deviation of sample =", numpy.std(sample))
        
        
    return popMean, sampleMean, numpy.std(population), numpy.std(sample)

    
random.seed(0)

temps = getHighs()

popMean = sum(temps) / len(temps)

sampleSize = 200

numTrials = 10000

numBad = 0

for t in range(numTrials):
    
    sample = random.sample(temps, sampleSize)
    
    sampleMean = sum(sample) / sampleSize
    
    se = numpy.std(sample) / sampleSize ** 0.5
    
    if abs(popMean - sampleMean) > 1.96 * se:
        
        numBad += 1
        
        
print("Fraction outside 95% confidence interval =", numBad / numTrials)

     
for t in range(numTrials):
    
    popStartingPts = range(0, len(temps) - sampleSize)
    start = random.choice(popStartingPts)
    sample = temps[start: start + sampleSize]
    se = numpy.std(sample) / sampleSize ** 0.5
    
    
    if abs(popMean - sampleMean) > 1.96 * se:
        
        numBad += 1
        
print("Fraction outside 95% confdence interval =", numBad / numTrials)

        
    
    
    
    
    
    



        
        



        
        
        
        
        
        
        
        
        
    
    
        
            
    





    
    
    
    
    
    