#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 01:55:24 2024

@author: sheeraz
"""

# Program 6


class Food(object):
    
    def __init__(self, n, v, c):
        self.name = n
        self.value = v
        self.calories = c
        
        
    def getValue(self):
        return self.value
    
    def getCost(self):
        return self.calories
    
    def getDensity(self):
        return self.getValue() / self.getCost() 
        
    def __str__(self):
        self.name + ": <" + str(self.value) + ", " + str(self.calories) + ">"
       
def buildMenu(names, values, calories):
      
    menu = []
    
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
       
    return menu

def maxVal(toConsder, avail):
    
    """Assumes to consder a list of items, avail a weight
       returns a tuple of the total weight of a solution to the
       0/1 knapsack and the items of that solution"""
       
    if toConsder == [] or avail == 0:
        result = (0, ())
       
    elif toConsder[0].getCost() > avail:
       
         # Explore right branch only
         result = maxVal(toConsder[1:], avail)
        
    else:
        nextItem = toConsder[0]
        
        # Explore left branch
        withVal, withToTake = maxVal(toConsder[1:], avail - nextItem.getCost())
        
        withVal += nextItem.getValue()
        
        # Explore right branch
        withoutVal, wthoutToTake =  maxVal(toConsder[1:], avail)
        
        # Choose better branch
        if withVal > withoutVal:
            result = (withVal, wthoutToTake + (nextItem,))
        else:
            result = (withoutVal, wthoutToTake)
            
    
    return result 


import random


def buildLargeMenu(numItems, maxVal, maxCost):
    
    items = []
    
    for i in range(numItems):
        items.append(Food(str(i), random.randint(1, maxVal), random.randint(1, maxCost)))
        
        
    return items


def fastMaxVal(toConsder, avail, memo = {}):
    
    """Assumes toConsder list of subjects, avail a weight
       memo supplied by recursive  calls
       returns a tuple of the total value of a solution to the
       0/1 knapsack problem and the subjects of that solution"""
       
    if ((len(toConsder), avail) in memo):
        result = memo[(len(toConsder), avail)]
        
    elif toConsder == [] or avail == 0:
        
        result = (0, ())
        
    elif toConsder[0].getCost() > avail:
        
        # Explore right branch only
        result = fastMaxVal(toConsder[1:], avail, memo)
        
    else:
        nextItem = toConsder[0]
        
        # Explore left branch
        withVal, withToTake = fastMaxVal(toConsder[1:], avail - nextItem.getCost(), memo)
        
        withVal += nextItem.getValue()
        
        # Explore right branch 
        withoutVal, withoutToTake = fastMaxVal(toConsder[1:], avail, memo)
        
        # Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
            
            
        else:
            result = (withoutVal, withoutToTake)
            
    memo[(len(toConsder), avail)] = result
    
    return result


def testMaxVal(foods, maxUnits, algorithm, printItems = True):
    
    print("Menu contains", len(foods), "items")
    
    print("Use search tree to allocate", maxUnits, "calories")
    
    
    val, taken = algorithm(foods, maxUnits) 
    
    if printItems:
        print("Total value of items taken", val)
        
        for item in taken:
            print("   ", item)
            
  
# for numItems in [5, 10, 15, 20, 25, 30, 35, 40, 45]:
    
    # items = buildLargeMenu(numItems, 90, 250)
    # testMaxVal(items, 750, maxVal, False)
    
    
# Change code to keep track of number of calls
def countingFastMaxVal(toConsider, avail, memo = {}):
    
    """Assumes toConsder a list of subjects, avail a weight
       memo supplied by recursive calls
       returns a tuple of the total value of a solution to the
       0/1 knapsack problen and the subjects of that solution"""
       
       
    global numCalls
    
    numCalls += 1
    
    
    if (len(toConsider), avail) in memo:
        result = memo[(len(toConsider), avail)]
      
    elif toConsider == [] or avail == 0:
        result = (0, ())
        
    elif toConsider[0].getCost() > avail:
        
        # Explore right branch only
        result = countingFastMaxVal(toConsider[1:], avail, memo)
        
    else:
        nextItem = toConsider[0]
        
        # Explore left branch
        withVal, withToTake = countingFastMaxVal(toConsider[1:], avail - nextItem.getCost(), memo)
        
        
        withVal += nextItem.getValue()
        
        # Explore right branch
        withoutVal, withoutToTake = countingFastMaxVal(toConsider[1:], avail, memo)
        
        
       
        # Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,)) 
        else:
            result = (withoutVal, withoutToTake)
            
        
    memo[(len(toConsider), avail)] = result
    
    return result

for numItems in (2, 4, 8, 16, 32, 64, 128, 256, 512, 1024):
    
    numCalls = 0
    items = buildLargeMenu(numItems, 90, 250)
    
    testMaxVal(items, 750, countingFastMaxVal, False)
    print("Number of calls =", numCalls)
    

# Useless titanic
    
    
print(2016 - 2024)
print(2024 - 6)
    

print(2018 - 46)
print(2016 - 48)


print(2016 - 46)
print(2018 - 48)

print(1970 - 1912)
print(1968 - 1910)

# karte jao karte jao

print(1910 - 58)

# problem in indian and europan development
# if you can't then why are you claim for that?

# in results america and isreal problem  













    
    
    
    
    
        
        
      
        
      
        
      
        
      
        
      
        
    
    
    
    
    
    
   

                 
        
        
        
    
    
    
    

    

        
        
        
        
        
        
       
       
    
    
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       
       
       
       
       
       
       
       
       
       
            