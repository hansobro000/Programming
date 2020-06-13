# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 15:02:28 2020

@author: Brooks Hanson
"""

def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            if alist[location]>alist[positionOfMax]:
                positionOfMax = location

        alist[positionOfMax],alist[fillslot] = \
                   alist[fillslot],alist[positionOfMax]