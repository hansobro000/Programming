# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 14:58:14 2020

@author: Brooks Hanson
"""

def hash(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos])

    return sum%tablesize