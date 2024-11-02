#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 15:54:31 2024

@author: sheeraz
"""

# Program 4

class Food(object):
    
    def __init__(self, n, v, c):
        self.name = n
        self.value = v
        self.calories = c
        
    def getValue(self):
        return self.value
    
    def getCost(self):
        return self.calories
    
    def densty(self):
        return self.getValue() / self.getCost()
    
    def __str__(self):
        return self.name + ":  <" + str(self.value) + ", " + str(self.calories) + ">"
    


def buildMenu(names, values, calories):
    
    menu = []
    
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
        
    return menu

 
def greedy(items, maxCost, keyFunction):
    
    """Assumes items a list, maxCost >= 0,
       eyFunction maps elements of items to numbers"""
       
    itemsCopy = sorted(items, key=keyFunction, reverse=True)
    
    result = []
    
    totalValue, totalCost = 0.0, 0.0
    
    
    for i in range(len(itemsCopy)):
        
        if (totalCost+itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()
            
    return (result, totalValue)


def testGreedy(items, constraint, keyFunction):
    
    taken, val = greedy(items, constraint, keyFunction)
    print("Total value of items taken =", val)
    
    for item in taken:
        print("   ", item)
        
        
    
def testGreedys(foods, maxUnits):
        
    print("Use greedy by value to allocate", maxUnits, "calories")
    testGreedy(foods, maxUnits, Food.getValue)
    
    print("\nUse greedy by cost to allocate", maxUnits, "calories")
    testGreedy(foods, maxUnits, lambda x: 1 / Food.getCost(x))
    
    print("\nUse greedy by density to allocate", maxUnits, "calories")
    testGreedy(foods, maxUnits, Food.densty)
    
    
def maxVal(toConsder, avail):
    
    """Assumes toConsder a list of items, avail a weight
       returns a tuple of the total value of a soluton to the
       0/1 knapsack problem and the items of that solution"""
       
    
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
        withoutVal, withoutToTake = maxVal(toConsder[1:], avail)
        
        # Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withToTake)
            
            
    return result



def testMaxVal(foods, maxUnits, printItems = True):
    
    print("Use search tree to allocate", maxUnits, calories)
    
    val, taken = maxVal(foods, maxUnits) 
    print("Total value of items taken =", val)
    
    if printItems:
        for item in taken:
           print("   ",item)
           
           
names = ["wine", "beer", "pizza", "burger", "fries", "cola", "apple", "donut", "cake"]

values = [89, 90, 95, 100, 90, 79, 50, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]
foods = buildMenu(names, values, calories)

testGreedys(foods, 750)
print(" ")
testMaxVal(foods, 750)


    
    
    
    
 
    
    
    




        
            
            
        
        
        
    
    

    
    
    
    
    
    
    
    
    
    
    
        
            
            
        
    
    
    
    
    
    
    
    
    
    
    
       
       
       
    
    
            
    
    
    