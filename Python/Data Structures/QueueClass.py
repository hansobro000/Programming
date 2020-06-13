# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 13:28:06 2020

@author: Brooks Hanson
"""
#%%
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 09:41:02 2019

@author: matth
"""
#%%

#Queue implementation using a python list.

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)