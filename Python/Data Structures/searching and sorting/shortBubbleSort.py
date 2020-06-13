# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 15:01:46 2020

@author: Brooks Hanson
"""

def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if alist[i]>alist[i+1]:
               exchanges = True
               alist[i],alist[i+1]=alist[i+1],alist[i]
       passnum = passnum-1