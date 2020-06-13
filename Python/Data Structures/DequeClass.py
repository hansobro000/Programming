# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 13:31:48 2020

@author: Brooks Hanson
"""
#%%
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 07:29:13 2019

@author: matth
"""
#%%

class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)
    
    def peekFront(self):
        return self.items[0]
    
    def peekRear(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)