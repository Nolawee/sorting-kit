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
import matplotlib.pyplot as plt


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

def quickSort(lst):
    # TODO: Implement quicksort here
    # You may add additional utility functions to help you out.
    # But the function to do quicksort should be called quickSort
    if (len(lst) <= 1):
        return lst
    (q, plst) = randPartition(lst)
    left = quickSort(plst[0:q])
    right = quickSort(plst[q + 1:len(plst)])
    left.append(plst[q])
    return left + right

def randPartition(lst):
    pivotP = random.randint(0, len(lst) - 1)
    lst[len(lst) - 1], lst[pivotP] = lst[pivotP], lst[len(lst) - 1]
    return partition(lst)

def partition(lst):
    i = -1
    pivot = lst[len(lst) - 1]
    for j in range(0, len(lst) - 1):
        if (lst[j] <= pivot):
            i += 1
            lst[j], lst[i] = lst[i], lst[j]
    i += 1
    lst[len(lst) - 1], lst[i] = lst[i], lst[len(lst) - 1]
    return (i, lst)


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

def runningTime():

    insertionAverage = []
    mergeAverage = []
    quickAverage = []

    insertionWorst = []
    mergeWorst = []
    quickWorst = []

    n = []

    for i in range(5, 505, 5):
        insertionTimes = []
        mergeTimes = []
        quickTimes = []

        worstInsertionTimes = []
        worstMergeTimes = []
        worstQuickTimes = []

        for j in range(0,20):
            random = generateRandomList(i)

            #quickReversed = []
            #mergeReversed = []
            #insertionReversed = []

            for k in range(0, i):
                #quickReversed.append(i)
                #mergeReversed.append(i)
                #insertionReversed.append(i)

            #quickReversed.reverse()
            #mergeReversed.reverse()
            #insertionReversed.reverse()


            #quickTime = measureRunningTimeComplexity(quickSort, random)
            #mergeTime = measureRunningTimeComplexity(mergeSort, random)
            #insertionTime = measureRunningTimeComplexity(insertionSort, random)

            #quickTimes.append(quickTime)
            #mergeTimes.append(mergeTime)
            #insertionTimes.append(insertionTime)

            #quickTime = measureRunningTimeComplexity(quickSort, quickReversed)
            #mergeTime = measureRunningTimeComplexity(mergeSort, mergeReversed)
            #insertionTime = measureRunningTimeComplexity(insertionSort, insertionReversed)

            #worstQuickTimes.append(quickTime)
            #worstMergeTimes.append(mergeTime)
            #worstInsertionTimes.append(insertionTime)

        #averageQuick = sum(quickTimes)/float(len(quickTimes))
        #quickAverage.append(averageQuick)
        #worstQuick = sum(worstQuickTimes)/float(len(worstQuickTimes))
        #quickWorst.append(worstQuick)

        
        #averageMerge = (sum(mergeTimes))/float(len(mergeTimes))
        #mergeAverage.append(averageMerge)
        #worstMerge = sum(worstMergeTimes)/float(len(worstMergeTimes))
        #mergeWorst.append(worstMerge)


        #averageInsertion = sum(insertionTimes)/float(len(insertionTimes))
        #insertionAverage.append(averageInsertion)
        #worstInsertion = sum(worstInsertionTimes)/float(len(worstInsertionTimes))
        #insertionWorst.append(worstInsertion)

        n.append(i)

        #del insertionTimes
        #del mergeTimes
        #del quickTimes

        #del worstInsertionTimes
        #del worstMergeTimes
        #del worstQuickTimes

    plt.plot(n, quickAverage, 'bs')
    plt.plot(n, quickWorst, 'ro')

    plt.ylabel('average/worst-case time (seconds)')
    plt.xlabel('lists size n')

    plt.title('Time table of QuickSort')

    plt.show()

runningTime()



