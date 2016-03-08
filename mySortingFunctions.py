# Name: Nolawee Mengist
# Email: nome9478@colorado.edu
# SUID: 102592298
#
# By submitting this file as my own work, I declare that this
# code has been written on my own with no unauthorized help. I agree to the
# CU Honor Code. I am also aware that plagiarizing code may result in
# a failing grade for this class.
from __future__ import print_function
import sys
import random
import time
import numpy


# --------- Insertion Sort -------------
# Implementation of getPosition
# Helper function for insertionSort
def getPosition(rList, elt):
    # Find the position where element occurs in the list
    #
    for (i,e) in enumerate(rList):
        if (e >= elt):
            return i
    return len(rList)

# Implementation of Insertion Sort 
def insertionSort(lst):
    n = len(lst)
    retList = []
    for i in lst:
        pos = getPosition(retList,i)
        retList.insert(pos,i)    
    return retList

#------ Merge Sort --------------

def merge (left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left [i:]
    result += right [j:]
    return result

def mergeSort (lst):
    if len (lst) <= 1:
        return lst
    middle = int (len (lst)/2)
    #print(lst)
    #print(middle)
    left = mergeSort (lst[:middle])
    right = mergeSort (lst[middle:])
    return merge(left, right)

#------ Quick Sort --------------

def quickSort (lst):
    if lst == []:
        return []
    else:
        smallsorted = quickSort([x for x in lst[1:] if x <= lst[0]])
        bigsorted   = quickSort([x for x in lst[1:] if x >  lst[0]])
        return smallsorted + [lst[0]] + bigsorted

'''
def quickSort(lst):
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[0]
        del(lst[0])

        lst_l = []
        lst_r = []

        for number in lst:
            if number < pivot:
                lst_l.append(number)
            else:
                lst_r.append(number)
        lstFinal = quickSort(lst_l)+[pivot]+quickSort(lst_r) 
        return lstFinal 

lst = [10, 329, 821 ,721, 663, 55, 23, 324, 212, 121]
newlst = quickSort(lst)
print(newlst)
'''


# ------ Timing Utility Functions ---------

# Code below is given only for demonstration purposes

# Function: generateRandomList
# Generate a list of n elements from 0 to n-1
# Shuffle these elements at random

def generateRandomList(n):
   # Generate a random shuffle of n elements
   lst = list(range(0,n))
   random.shuffle(lst)
   return lst


def measureRunningTimeComplexity(sortFunction,lst):
    t0 = time.clock()
    sortFunction(lst)
    t1 = time.clock() # A rather crude way to time the process.
    return (t1 - t0)

def worstCase(sortFunction):
    #make arrays to store index values and to store timeComplexity values
    timePlots = []
    sizePlots = []
    #make randomized lists/find time complexity for each list
    for i in xrange(0,20):
        n = random.randint(1,100)*5
        #print n
        sizePlots.append(n)
        lst = generateRandomList(n)
        #appending time and number elements to appropriate arrays
        sortFunctionName = sortFunction.__name__
        timeComplexity = measureRunningTimeComplexity(sortFunction,lst)
        timePlots.append(timeComplexity)
    #print(n)
    print("This is the array for all sizes of arrays {}".format(sizePlots))
    #print("{} has a worst case running time of {} seconds".format(sortFunctionName, max(timePlots)))
    return max(timePlots)
worstCase(mergeSort)
worstCase(quickSort)

def averageCase(sortFunction):
    timePlots = []
    sizePlots = []
    for i in xrange(0,20):
        n = random.randrange(5,500,5)
        #print n
        sizePlots.append(n)
        lst = generateRandomList(n)
        #appending time and number elements to appropriate arrays
        sortFunctionName = sortFunction.__name__
        timeComplexity = measureRunningTimeComplexity(sortFunction,lst)
        timePlots.append(timeComplexity)
    #print("{} has an average case running time of {} seconds".format(sortFunctionName, numpy.mean(timeComplexity)))
    return numpy.mean(timeComplexity)
averageCase(mergeSort)
averageCase(quickSort)



# --- TODO

# Write code to extract average/worst-case time complexity for your sorting routines.
'''
timePlots = []
sizePlots = []
for i in xrange(0,20):
    n = random.randrange(5,500,5)
    sizePlots.append(n)
    #print(n)
    lst = generateRandomList(n)
    #print(lst)
    timeComplexity = measureRunningTimeComplexity(mergeSort,lst)
    timePlots.append(timeComplexity)
    #print("{} seconds".format(timeComplexity))
    #print("=======================")
finalSizePlots = quickSort(sizePlots)
finalTimePlots = quickSort(timePlots)
#for i in xrange(0,len(finalSizePlots)):
    #print("({} elements, {} seconds)".format(finalSizePlots[i],finalTimePlots[i]))



lst = generateRandomList(n)
print(lst)

timeComplexity = measureRunningTimeComplexity(quickSort,lst)
print(timeComplexity)
'''


