# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 18:48:39 2020

@author: Brooks Hanson
"""

#%%
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 13:14:00 2019

@author: matth
"""
from NodeClass import *

class unorderedList:
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return(self.head == None)
        
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        
    def length(self):
        current = self.head
        count = 0
        while current != None:
            count = count +1
            current = current.getNext()
        return(count)
        
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.data == item:
                found = True
            else:
                current = current.getNext()
        return(found)
        
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found and current != None:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
                
        if current == None and not found:
            raise ValueError("Value not found.")
        
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())