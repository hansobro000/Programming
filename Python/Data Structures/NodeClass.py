# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 13:08:58 2019

@author: matth
"""

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
        
    def getData(self):
        return(self.data)
        
    def getNext(self):
        return(self.next)
        
    def setData(self,newdata):
        self.data = newdata
    
    def setNext(self,newnext):
        self.next = newnext
