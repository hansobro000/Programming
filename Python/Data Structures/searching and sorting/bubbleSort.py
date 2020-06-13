# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 15:01:18 2020

@author: Brooks Hanson
"""

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1]=alist[i+1],alist[i]