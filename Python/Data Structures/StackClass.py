# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 13:43:24 2020

@author: Brooks Hanson
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 18:25:45 2019

@author: matth
"""

#Stack implementation using a python list.

class Stack:
    def __init__(self, name):
        self.items = []
        self.name = name

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() #built in function, returns item at end
                                #destructive, no longer on stack
    def peek(self):
        return self.items[len(self.items)-1]
                                #non-destructive, just see whats on top
    def size(self):
        return len(self.items)
    
    def __str__(self):
        string = ""
        for i in self.items:
            string = string + str(i)+ " "
        return(string)
    
