# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 14:44:30 2020

@author: Brooks Hanson
"""

def sequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos+1

    return found