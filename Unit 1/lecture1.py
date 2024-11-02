#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 19:42:30 2024

@author: sheeraz
"""

# Program 1



class Food(object):
    
    
    def __init__(self, n, v, w):
       self.name = n
       self.value = v
       self.calories = w
       
    def getValue(self):
        return self.value
    
    def getCost(self):
        return self.calories
    
    def density(self):
        return self.getValue() / self.getCost()
    
    def __str__(self):
        return self.name + ': <' + str(self.value) + ', ' + str(self.calories) + '>'
       
    
    
     
    
def buildMenu(names, values, calories):
    
    
    """names, values, calories lists of the same length.
       name a list of strings,
       values and calories list of numbers
       returns lst of Food"""
       
       
    menu = [] 
    
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
        
    return menu


def greedy(items, maxCosts, keyFuncton):
    
    """Assumes items a list, maxCosts >= 0,
       keyFuncton maps elements of items to numbers"""     
       
    itemsCopy = sorted(items, key= keyFuncton, reverse=True)
    
    result = []
    
    totalValue, totalCost = 0.0, 0.0
    
    for i in range(len(itemsCopy)):
        
        if (totalCost + itemsCopy[i].getCost()) <= maxCosts:
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
    
    testGreedy(foods, maxUnits, lambda x: 1/Food.getCost(x))
    print("\nUse greedy by density to allocate", maxUnits, "calories")
    
    
    testGreedy(foods, maxUnits, Food.density)
    
    
    
names = ["wine", "beer", "pizza", "burger", "fries",
                 "cola", "apple", "apple", "donut", "cake"]

values = [89, 90, 95, 100, 90, 79, 50, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]

foods = buildMenu(names, values, calories) 

testGreedys(foods, 1000)

