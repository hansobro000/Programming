# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 15:28:14 2020

@author: Brooks Hanson
"""
#%%
#reset environment
from IPython import get_ipython

get_ipython().magic('reset -sf')

#%%
#import necessary libraries
from random import *
import timeit
import statistics

#%%
#from canvas
def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            if alist[location]>alist[positionOfMax]:
                positionOfMax = location

        alist[positionOfMax],alist[fillslot] = \
                   alist[fillslot],alist[positionOfMax]

#%%
#from canvas
def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

      sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and \
                alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap] 
            position = position-gap

        alist[position]=currentvalue

#%%
#from canvas
def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first<last:

        splitpoint = partition(alist,first,last)

        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
    pivotvalue = alist[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and \
                alist[leftmark] < pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] > pivotvalue and \
                rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark],alist[rightmark]= \
                         alist[rightmark],alist[leftmark]

    alist[first],alist[rightmark]= \
                   alist[rightmark],alist[first]

    return rightmark

#%%
#building off of wrapper code from PythonCentral
#wrapper helps pass function and arguments

#create random list of 500 integers
randomList = sample(range(1000),500)

#function to create a text file and write to it
def writeFile(sl,fname):
    with open(fname, 'w') as f:
        for item in sl:
            f.write("%s\n" % item)

#function to read a text file
def readList(l):
    with open('chapter5randomlist.txt', 'r') as infile:
        for line in infile:
            i = int(line.strip('\n'))
            l.append(i)

#write the random list to a text file
writeFile(randomList, "chapter5randomlist.txt")

#function to time any sorting method, providing grounds for benchmark analysis 
def wrapTimer(sortMethod):
    #read from text file containing 500 random integers, now contained in l
    l = []
    readList(l)
    
    #create text version of sorting method name for use in print statement
    m = str(sortMethod).upper().split()
    
    #Wrapper function to allow timeit.repeat to accept a function
    #while passing l as the parameter    
    def wrapper(func, *args, **kwargs):
        def wrapped():
            return func(*args, **kwargs)
        return wrapped
    
    #implement wrapper function to wrap l into the chosen sort method
    wrapper = wrapper(sortMethod, l)
    
    #use timeit.repeat to measure how long it takes to execute the desired 
    #sort method 100 times, repeating the process 5 different times.
    wrapTime = timeit.repeat(wrapper, repeat=5, number=100)
    
    #print the times of the 5 repetitions as well as the mean of those 5 times
    print("\nFor a random list of 500 integers, the number of seconds to sort",
          "using {0} method 100 times; 5 tries:\n".format(m[1]), wrapTime, 
          "\n\n{0} mean execution time in seconds:\n".format(m[1]), 
          statistics.mean(wrapTime))

#Implement the wrapTimer function for each of the three desired sorting methods
wrapTimer(quickSort)
wrapTimer(shellSort)
wrapTimer(selectionSort)

#Output

########

#For a random list of 500 integers, the number of seconds to sort using 
#QUICKSORT method 100 times; 5 tries:
# [2.178135300000008, 2.553720499999997, 2.281516300000021,
#  2.9162702000000422, 1.1269570000000044] 

#QUICKSORT mean execution time in seconds:
# 2.211319860000015

#For a random list of 500 integers, the number of seconds to sort using 
#SHELLSORT method 100 times; 5 tries:
# [0.08803690000002007, 0.08786010000000033, 0.09126520000000937, 
#  0.08878149999998186, 0.08915239999998903] 

#SHELLSORT mean execution time in seconds:
# 0.08901922000000013

#For a random list of 500 integers, the number of seconds to sort using 
#SELECTIONSORT method 100 times; 5 tries:
# [0.8308787999999936, 1.5149573999999575, 2.2314559000000145, 
#  1.4658046000000127, 1.4989105999999879] 

#SELECTIONSORT mean execution time in seconds:
# 1.5084014599999933

########

#As the output shows, the Shell Sort method for sorting is the fastest way to 
#sort the 500 random integers (0.0890 seconds). The second fastest is the 
#Selection Sort method (1.5084 seconds) followed by the Quick Sort method which
#results in a time of (2.2113 seconds). 

#One thing to note about these times is that the wrapper function used to 
#allow for a function with a parameter pass takes a good deal of time. With
#that said, it is a constant between all three types of sorting, so an 
#equivalent amount of time is taken on that piece of the wrapTimer function.

#The results that I have gotten are contradictory to the simulation results on
#Toptal.com. In a true random environment, as similuated here, Shell Sort
#should be the fastest, closely followed by Quick Sort, with Selection Sort
#trailing far behind. My simulations correctly had Shell Sort performing 
#consistently the best, but Quick Sort drastically underperforming. 
#%%
