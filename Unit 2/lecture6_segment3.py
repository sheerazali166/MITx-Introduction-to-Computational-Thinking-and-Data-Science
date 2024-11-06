#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 05:43:36 2024

@author: sheeraz
"""

import random, pylab

# set line width
pylab.rcParams["lines.linewidth"] = 4

# set font size for titles
pylab.rcParams["axes.titlesize"] = 20

# set font size for labels on axis
pylab.rcParams["axes.labelsize"] = 20

# set size of numbers on x-axis
pylab.rcParams["xtick.labelsize"] = 16

# set size of numbers on y-axis
pylab.rcParams["ytick.labelsize"] = 16

# set size of thicks on x-axis
pylab.rcParams["xtick.major.size"] = 7

# set size of thicks on y-axis
pylab.rcParams["ytick.major.size"] = 7

# set size of markers, e.g, circles representing points
# set numpoints for legend
pylab.rcParams["legend.numpoints"] = 1


class Location(object):
    
    def __init__(self, x, y):
        
        """x and y are numbers"""
        
        self.x = x
        self.y = y
        
    def move(self, deltaX, deltaY):
        
        """deltaX and and deltaY are numbers"""
        return Location(self.x + deltaX, self.y + deltaY)
             
    
     
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def distFrom(self, other):
        ox = other.x
        oy = other.y
        
        xDist = self.x - ox
        yDist = self.y - oy
        
        return (xDist ** 2 + yDist ** 2) ** 0.5
    
    def __str__(self):
        return "<" + str(self.x) + ", " + str(self.y) + ">"
    
    
        
class Field(object):
    
    def __init__(self):
        self.drunks = {}
        
    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError("Duplicate drunk")
        else:
            self.drunks[drunk] = loc
            
    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError("Drunk not in field")
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        
        # use move method of location to get new location
        self.drunks[drunk] = currentLocation.move(xDist, yDist)
        
    def getLoc(self, drunk):
        
        if drunk not in self.drunks:
            raise ValueError("Drunk not in field")
        return self.drunks[drunk]


class Drunk(object):
    
    def __init__(self, name = None):
        """Assumes name is a str"""
        self.name = name
        
    def __str__(self):
        if self != None:
            return self.name
        return "Anonymous"
    
class UsualDrunk(Drunk):
    
    def takeStep(self):
        stepChoices = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        return random.choice(stepChoices)
        
        
def walk(f, d, numSteps):
    
    """Assumes: f a Field, d a Drunk in f, and numSteps an int >= 0.
       moves d numSteps times, and returns the distance between the
       final location and the location at the start of the walk."""
       
    start = f.getLoc(d)
    
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))

def simWalks(numSteps, numTrials, dClass):
    
    """Assumes numSteps an int >= 0, numTrial an int > 0,
       dClass a subclass of Drunk simulates numTrals walks
       of numSteps steps each. returns a list of the final
       distances for each trials"""
       
    Homer = dClass()
    
    origin = Location(0, 0)
    distances = []
    
    for t in range(numTrials):
        f = Field()
        f.addDrunk(Homer, origin)
        
        distances.append(round(walk(f, Homer, numSteps), 1))

    return distances

def drunkTest(walkLengths, numTrials, dClass):
    
    """Assumes walkLengths a sequence of ints >= 0
       numTrials an int > 0, dClass a subClass of Drunk
       for each number of steps in walkLengths, runs simWalks
       with numTrials walks and prints results"""
       
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials, dClass)
        print(dClass.__name__, "random walk of numSteps", numSteps, "steps")
        print(" Mean =", round(sum(distances) / len(distances), 4))
        print(" Max=", max(distances), "Min=", min(distances))
        
        
# random.seed(0)
# drunkTest((10, 100, 1000, 10000), 100, UsualDrunk)

class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0, 0.9), (0.0, -1.1), (1.0, 0.0), (-1.0, 0.0)]
        
        return random.choice(stepChoices)

def simAll(drunKinds, walkLengths, numTrials):
    for dClass in drunKinds:
        drunkTest(walkLengths, numTrials, dClass)
        
# random.seed(0)

# simAll((UsualDrunk, ColdDrunk), (1, 10, 100, 1000, 10000), 100)


# Random Walks and More Plotting, Segment 3

# Previous Segments

# Presented a related collection of data abstractions

# Talked about structuring and testing simulations

# Printed the results of some simulations

# Iterating Over Styles

class styleIterator(object):
    def __init__(self, styles):
        self.index = 0
        self.styles = styles
        
    def nextStyle(self):
        result = self.styles[self.index]
        if self.index == len(self.styles) - 1:
            self.index = 0
        else:
            self.index += 1
            
        return result


# simDrunk

def simDrunk(numTrials, dClass, walkLengths):
    meanDistances = []
    for numSteps in walkLengths:
        print("Starting simulation of", numSteps, "steps")
        
        trials = simWalks(numSteps, numTrials, dClass)
        mean = sum(trials) / len(trials) 
        meanDistances.append(mean)
    return meanDistances


# simAll (new version)

def simAll(drunkKinds, walkLengths, numTrials):
    styleChoice = styleIterator(("m-", "b--", "g-."))
    
    for dClass in drunkKinds:
        curStyle = styleChoice.nextStyle()
        print("Starting simulation of", dClass.__name__)
        means = simDrunk(numTrials, dClass, walkLengths)
        pylab.plot(walkLengths, means, curStyle, label = dClass.__name__)
        pylab.title("Mean Distance from Origin (" + str(numTrials) + " trials)")
        
        pylab.xlabel("Number of Steps")
        pylab.ylabel("Distance from Origin")
        pylab.legend(loc = "best")
  
          
numSteps = (10, 100, 1000, 10000)
simAll((UsualDrunk, ColdDrunk), numSteps, 100)

# Getting Ends of Multiple Walks

def getFinalLocks(numSteps, numTrials, dClass):
    
    locs = []
    d = dClass()
    
    for t in range(numTrials):
        f = Field()
        f.addDrunk(d, Location(0, 0))
        
        for s in range(numSteps):
            f.moveDrunk(d)
            locs.append(f.getLoc(d))
    return locs        
        
# Plotting Ending Locations

def plotLocs(drunkKinds, numSteps, numTrials):
    styleChoice = styleIterator(("k+", "r^", "mo"))
    
    for dClass in drunkKinds:
        locs = getFinalLocks(numSteps, numTrials, dClass)
        xVals, yVals = [], []
        
        for loc in locs:
            xVals.append(loc.getX())
            yVals.append(loc.getY())
            
        xVals = pylab.array(xVals)
        yVals = pylab.array(yVals)
        
        meanX = sum(abs(xVals)) / len(xVals)
        meanY = sum(abs(yVals)) / len(yVals)
        
        curStyle = styleChoice.nextStyle()
        pylab.plot(xVals, yVals, curStyle, label = dClass.__name__ +
                   " means abs dist = <" + str(meanX) + ", " + str(meanY)
                       + ">")
        
    pylab.title("Location at End of Walks (" + str(numSteps) + " steps)")

    pylab.ylim(-1000, 1000)
    pylab.xlim(-1000, 1000)
    pylab.xlabel("Steps East/West of Origin")
    pylab.ylabel("Steps North/South of Origin")
    pylab.legend(loc = "upper left")

random.seed(0)
plotLocs((UsualDrunk, ColdDrunk), 10000, 1000)    
        
        
# A Subclass of Field, part 1

class OddField(Field):
    
    def __init__(self, numHoles = 1000, xRange = 100, yRange = 100):
        
        Field.__init__(self)
        self.wormholes = {}
        
        
        for w in range(numHoles):
            x = random.randint(-xRange, xRange)
            y = random.randint(-yRange, yRange)
            
            newX = random.randint(-xRange, xRange)
            newY = random.randint(-yRange, yRange)
            
            newLoc = Location(newX, newY)
            self.wormholes[(x, y)] = newLoc
            
            
    def moveDrunk(self, drunk):
        
        Field.moveDrunk(self, drunk)
        x = self.drunks[drunk].getX()
        y = self.drunks[drunk].getY()
        
        if (x, y) in self.wormholes:
            self.drunks[drunk] = self.wormholes[(x, y)]
           
# TraceWalk using oddField
def traceWalk(fieldKinds, numSteps):
    styleChoice = styleIterator(("b+", "r^", "ko"))

    for fClass in fieldKinds:
        d = UsualDrunk()
        f = fClass()
        f.addDrunk(d, Location(0, 0))
        
        locs = []
        
        for s in range(numSteps):
            f.moveDrunk(d)
            locs.append(f.getLoc(d))

        xVals, yVals = [], []
        
        for loc in locs:
            xVals.append(loc.getX())
            yVals.append(loc.getY())
            
        curStyle = styleChoice.nextStyle()
        pylab.plot(xVals, yVals, curStyle, label = fClass.__name__)
        
        pylab.title("Spots Visited on Walk (" + str(numSteps) + " steps)")

        pylab.xlabel("Steps East/West of Origin")
        pylab.ylabel("Steps North/South of Origin")
        pylab.legend(loc = "best")
        
        
random.seed(0)
traceWalk((Field, OddField), 500)        

        
pylab.show()   

# Summary

    # Point is not the simulations themselves, but how we built them
    
    # Three classes corresponding to domain-specific types

        # ◦ Location
        # ◦ Field
        # ◦ Drunk
        
     # Functions corresponding to
     
        # ◦ One trial
        # ◦ Multiple trials
        # ◦ Result reporting
        
        
# Summary, cont.

# Created two subclasses of Drunk

# Simulation had an argument of type class, so we could easily investigate
# both classes of Drunk

# Made series of incremental changes to simulation so that we could
# investigate different questions

    # ◦ Get simple version working first
    # ◦ Elaborate a step at a time

# Introduced a weird subclass of Field

    # ◦ Easy to add to simulation
    # ◦ Would have been hard to model analytically


# Coming Up Next

# We spent this lecture looking at a simulation and using it to draw some
# conclusions

# Time to get serious about stochastic simulations

# ◦ Probabilistic thinking
# ◦ Understanding how much confidence we should have in the result of a
#   simulation








        
 
    
 
    
 
    
 
        
        
        
        
        
        
    
 
        
        






    
            
        