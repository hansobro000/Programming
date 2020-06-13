# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 14:57:28 2020

@author: Brooks Hanson
"""

def binarySearchRecursive(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint]==item:
            return True
        else:
            if item<alist[midpoint]:
              return binarySearchRecursive(alist[:midpoint],item)
            else:
              return binarySearchRecursive(alist[midpoint+1:],item)