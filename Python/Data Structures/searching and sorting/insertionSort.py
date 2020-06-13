# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 15:02:52 2020

@author: Brooks Hanson
"""

def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue