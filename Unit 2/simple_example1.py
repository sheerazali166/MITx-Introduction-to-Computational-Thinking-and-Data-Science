#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 13:52:53 2024

@author: sheeraz
"""

# Program 1

# SIMPLE EXAMPLE

# basic function plots two lists as x and y values other data structures more
# powerful, use lists to demonstrate

# first, let’s generate some example data

import matplotlib.pyplot as plt

mySample = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(30):
    mySample.append(i)
    myLinear.append(i)
    myQuadratic.append(i ** 2)
    myCubic.append(i ** 3)
    myExponential.append(1.5 ** i)
    
    
# Select 1.5 to keep displays visible, more likely value for order of growth
# example would be 2

# to generate a plot, call  
plt.plot(mySample, myLinear)


# OVERLAPPING DISPLAYS

# suppose we want to display all of the graphs of the different orders
# of growth

# we could just call:
    
plt.plot(mySample, myLinear) 
plt.plot(mySample, myQuadratic) 
plt.plot(mySample, myCubic)
plt.plot(mySample, myExponential)  


# Impossble to see linear graph, or even quadratic graph


plt.plot(mySample, myLinear) 
plt.plot(mySample, myQuadratic) 
plt.plot(mySample, myCubic)
plt.plot(mySample, myExponential)


# OVERLAPPING DISPLAYS

# not very helpful, can’t really see anything but the biggest of the plots
# because the scales are so different

# can we graph each one separately?

# call

# plt.figure(<arg>)
           # -----
           
# gives a name to this figure; allows us to reference for future use

# creates a new display with that name if one does not already exist

# if a display with that name exists, reopens it for processing 

# EXAMPLE CODE

plt.figure("lin")
#----------------
plt.plot(mySample, myLinear)

plt.figure("quad")
#----------------
plt.plot(mySample, myQuadratic)

plt.figure("cube")
#----------------
plt.plot(mySample, myCubic)

plt.figure("expo")
#----------------
plt.plot(mySample, myExponential)


# SEPARATE PLOTS


plt.figure("lin")
#----------------
plt.plot(mySample, myLinear)
#---------------------------

# going to moon at my credit this is not fair

plt.figure("expo")
#-----------------
plt.plot(mySample, myExponential)
#--------------------------------

# PROVIDING LABELS

# Should really label the axes

plt.figure("lin")

plt.xlabel("sample points")
#--------------------------
plt.ylabel("linear function")
#----------------------------
# functions to label axes


plt.plot(mySample, myLinear)
plt.figure("quad")
#-----------------

plt.plot(mySample, myQuadratic)
plt.figure("cube")

plt.plot(mySample, myCubic)
plt.figure("expo")

plt.plot(mySample, myExponential)
plt.figure("quad")
#-----------------
plt.ylabel("quadratic function")
#-------------------------------

# note you must make figure active before invoking labeling


# LABELED AXES

# note no label on x axis as no invocation while that display was active
 

# ADDING TITLES

plt.figure("lin")
plt.plot(mySample, myLinear)
plt.figure("quad")
plt.plot(mySample, myQuadratic)
plt.figure("cube")
plt.plot(mySample, myCubic)
plt.figure("expo")
plt.plot(mySample, myExponential)




plt.figure("lin")
#----------------
plt.title("Linear")
#------------------
plt.plot(mySample, myLinear)


plt.figure("quad")
#-----------------
plt.title("Quadratic")
#------------------
plt.plot(mySample, myQuadratic)


plt.figure("cube")
#-----------------
plt.title("Cubic")
#-----------------
plt.plot(mySample, myCubic)


plt.figure("expo")
#-----------------
plt.title("Exponential")
#-----------------------
plt.plot(mySample, myExponential)


# TITLED DISPLAYS

# why are axes still labeled?
# why are colors the same in the two plots?


# CLEANING UP WINDOWS

# we are reusing a previously created display window
# need to clear it before redrawing

# because we are calling plot in a new version of a window, system starts
# with first choice of color (hence the same); we can control (see later)


# CLEANING WINDOWS

plt.figure("lin")
plt.clf()
#-------
plt.plot(mySample, myLinear)

plt.figure("quad")
plt.clf()
#--------
plt.plot(mySample, myQuadratic)

plt.figure("cube")
plt.clf()
#--------
plt.plot(mySample, myCubic)

plt.figure("expo")
plt.clf()
#--------
plt.plot(mySample, myExponential)


plt.figure("lin")
plt.title("Linear")
plt.figure("quad")
plt.title("Quadratic")
plt.figure("cube")
plt.title("Cubic")
plt.figure("expo")
plt.title("Exponential")


# COMPARING RESULTS

# now suppose we would like to compare different plots

# in particular, the scales on the graphs are very different

# one option is to explicitly set limits on the axis or axes

# a second option is to plot multiple functions on the same display



# CHANGING LIMITS ON AXES

plt.figure("lin")
plt.clf()
plt.ylim(0, 1000)
#----------------

plt.plot(mySample, myLinear)
plt.figure("quad")
plt.clf()
plt.ylim(0, 1000)
#----------------

plt.plot(mySample, myQuadratic)
plt.figure("lin")
plt.title("Linear")
plt.figure("quad")
plt.title("Quadratic")


# OVERLAYING PLOTS

plt.figure("lin quad")
plt.clf()
plt.plot(mySample, myLinear)
#---------------------------
plt.plot(mySample, myQuadratic)
#------------------------------

# each pair of calls within the same active display window

plt.figure("cube exp")
plt.clf()


plt.plot(mySample, myCubic)
#--------------------------
plt.plot(mySample, myExponential)
#--------------------------------

# each pair of calls within the same actve display window 

plt.figure("lin quad")
plt.title("Linear vs. Quadratic")
plt.figure("cube exp")
plt.title("Cubic vs. Exponential")


# ADDING MORE DOCUMENTATION

# can add a legend that identifies each plot
plt.figure("lin quad")
plt.clf()
plt.plot(mySample, myLinear, label = "linear")
                            # --------------- 
                            # label each plot
                            
plt.plot(mySample, myQuadratic, label = "quadratic")
                              # -------------------
                              
plt.legend(loc = "upper left")
# ----------------------------

plt.title("Linear vs. Quadratic")

# can specify a location


plt.figure("cube exp")
plt.clf()
plt.plot(mySample, myCubic, label="cubic")
                          # -------------
plt.plot(mySample, myExponential, label = "exponential")
                                # ---------------------
                                # can use best location
                            
plt.legend()
# ----------
plt.title("Cubic vs. Exponential")


# CONTROLLING DISPLAY PARAMETERS

# now suppose we want to control details of the displays themselves


# examples:

# changing color or style of data sets
# changing width of lines or displays
# using subplots


# CHANGING DATA DISPLAY

plt.figure("lin quad")
plt.clf()
plt.plot(mySample, myLinear, "b-", label = "linear")
                           # ----
plt.plot(mySample, myQuadratic, "ro", label = "quadratic")
                              # ---- 
plt.legend(loc = "upper left")
plt.title("Linear vs. Quadratic") 


plt.figure("cube exp")
plt.clf()
plt.plot(mySample, myCubic, "g^", label = "cubic")
                          # ----
plt.plot(mySample, myExponential, "r--", label = "exponential")
                                # -----
plt.legend()
plt.title("Cubic vs. Exponential")


# CHANGING DATA DISPLAY

plt.figure("lin quad")
plt.clf()
plt.plot(mySample, myLinear, "b-", label = "linear", linewidth = 2.0)
                                                   # ---------------
plt.plot(mySample, myQuadratic, "r", label = "quadratic", linewidth = 3.0)
                                                        # ---------------
# keyword can change size of parameter

plt.legend(loc = "upper left")
plt.title("Linear vs. Quadratic")

plt.figure("cube exp")
plt.clf()
plt.plot(mySample, myCubic, "g--", label = "cubic", linewidth = 4.0)
                                                  # ---------------- 
plt.plot(mySample, myExponential, "r", label = "exponential", linewidth = 5.0)
                                                            # ----------------
plt.legend()
plt.title("Cubic vs. Exponential")
                                                            

# USING SUBPLOTS

plt.figure("lin quad")
plt.clf()
plt.subplot(211)
# --------------
plt.ylim(0, 900)
# --------------

plt.plot(mySample, myLinear, "b-", label = "linear", linewidth = 2.0)
plt.subplot(212)
# -------------
plt.ylim(0, 900)
# --------------

plt.plot(mySample, myQuadratic, "r", label = "quadratic", linewidth = 3.0)
plt.legend(loc = "upper left")
plt.title("Linear vs. Quadratic")

plt.figure("cube exp")
plt.clf()

# arguments are number of rows & cols; and which location to use

# set limit within each subplot

plt.subplot(121)
# --------------
plt.ylim(0, 140000)
# -----------------

plt.plot(mySample, myCubic, "g--", label = "cubic", linewidth = 4.0)

plt.subplot(122)
# --------------
plt.ylim(0, 140000)
# -----------------

plt.plot(mySample, myExponential, "r", label = "exponential", linewidth = 5.0)
plt.legend()
plt.title("Cubic vs. Exponential")


# CHANGING SCALES

plt.figure("cube exp log")
plt.clf()
plt.plot(mySample, myCubic, "g--", label = "cubic", linewidth = 2.0)
plt.plot(mySample, myExponential, "r", label = "exponential", linewidth = 4.0)
plt.yscale("log")
# ---------------
# argument specifes type of scaling
 
plt.legend()
plt.title("Cubic vs. Exponential")

plt.figure("cube exp linear")
plt.clf()

plt.plot(mySample, myCubic, "g--", label = "cubic", linewidth = 2.0)
plt.plot(mySample, myExponential, "r", label = "exponential", linewidth = 4.0)
plt.legend()
plt.title("Cubic vs. Exponential")

plt.show()


# AN EXAMPLE

# want to explore how ability to visualize results can help guide computation

# simple example
# planning for retirement
# intend to save an amount m each month
# expect to earn a percentage r of income on investments each month

# want to explore how big a retirement fund will be compounded by time
# ready to retire


# AN EXAMPLE: compound interest

def retire(monthly, rate, terms):
    savings = [0]
    base = [0]
    mRate = rate / 12
    for i in range(terms):
        base += [i]
        savings += [savings[-1] * (1 + mRate) + monthly]
        
    return base, savings     
    

# DISPLAYING RESULTS vs. MONTH

def displayRetireWMonthlies(monthlies, rate, terms):
    plt.figure("retireMonth")
    plt.clf()
    
    # clear frame so can reuse
    
    for monthly in monthlies:
        xvals, yvals = retire(monthly, rate, terms)
        plt.plot(xvals, yvals, label = "retire:" + str(monthly))
                              # --------------------------------
                              # put informative label on each
        plt.legend(loc = "upper left")
           

displayRetireWMonthlies([500, 600, 700, 800, 900, 1000, 1100], 0.5, 40 * 12)


# DISPLAYING RESULTS vs. RATE

def displayRetireWRates(month, rates, terms):
    plt.figure("retireRate")
    plt.clf()
    
    for rate in rates:
        xvals, yvals = retire(month, rate, terms)
        plt.plot(xvals, yvals, label = "retire:" + str(month) + ":" + str(int(rate * 100)))
                             # ------------------------------------------------------------
                                         # put informative label on each 
                             
        plt.legend("upper left")
        
displayRetireWRates(800, [0.03, 0.05, 0.07], 40 * 12)


# ANALYSIS vs. RATE

# can also see impact of increasing expected rate of return on investments
# ranges from about 600K to 2.1M, as rate goes from 3% to 7%
# what if we look at both effects together?

# DISPLAYING RESULTS vs. BOTH

def displayRetireWMonthsAndRates(monthlies, rates, terms):
    plt.figure("retireBoth")
    plt.clf()
    plt.xlim(30 * 12, 40 * 12)
    # ------------------------
    # focus on last stages of fund
    
    for monthly in monthlies:
        for rate in rates:
            xvals, yvals = retire(monthly, rate, terms)
            plt.plot(xvals, yvals, label = "retre:" + str(monthly) + ":" + str(int(rate * 100)))
                                 # -------------------------------------------------------------
                                         # put informative label on each
            plt.legend(loc = "upper left")

displayRetireWMonthsAndRates([500, 700, 900, 1100], [0.3, 0.5, 0.7], 40 * 12)

# DISPLAYING RESULTS vs. BOTH

def displayRetireWMonthsAndRatesTwo(monthlies, rates, terms):
    plt.figure("retireBoth")
    plt.clf()
    plt.xlim(30 * 12, 40 * 12)
    
    monthLabels = ["r", "b", "g", "k"]
    # --------------------------------
    
    rateLabels = ["-", "o", "-"]
    # -------------------------
    
    # create sets of labels
    
    for i in range(len(monthlies)):
        monthly = monthlies[i]
        monthLabel = monthLabels[i % len(monthLabels)]
        # --------------------------------------------
        # pick new label for each month choice
        
        for j in range(len(rates)):
            rate = rates[j]
            rateLabel = rateLabels[j % len(rateLabels)]
            # -----------------------------------------
               # pick new label for each rate choice
            xvals, yvals = retire(monthly, rate, terms)
            plt.plot(xvals, yvals, monthLabel + rateLabel, label = "retire:"
                                 # ----------------------
                                 #  create label for plot
                                 
                     + str(monthly) + ":" + str(int(rate * 100)))
            
            plt.legend(loc = "upper left")
            
            
            
            
displayRetireWMonthsAndRatesTwo([500, 700, 900, 1100],
                                    [0.03, 0.05, 0.07], 40 * 12)   



plt.show()


# DISPLAYING RESULTS vs. BOTH

# now easier to see grouping of plots
    
# color encodes monthly contribute
# format (solid, circle, dashed) encodes growth rate of investments
        
# interaction with plotting routines and computations allows us to 
# explore data
    
# change display range to zero in on particular areas of interest
        
# change sets of values and visualize effect – then guides new choice
# of values to explore
        
# change display parameters to highlight clustering of plots by
# parameter
        

    
        
        
        








                      
        







 
  






