# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 13:36:20 2020

@author: Brooks Hanson
"""

#%%
#create queue
#create regular line
#create pre-check line
#send people from the queue to respective lines
#always process pre-check first

#%%
from QueueClass import *


line = ('p','r','p','p','r','r','r','p','r','r','r','r','p')
    
def split(line):
    
    regularQ = Queue()
    preQ = Queue()
    
    for i in line:
        if i == 'p':
            preQ.enqueue(i)
        elif i == 'r':
            regularQ.enqueue(i)
    return(regularQ,preQ)

def board(reg,pre):
    
    boardinglist = ()
    
    while pre.isEmpty() == False:
        boardinglist.append(pre.dequeue())
    
    while reg.isEmpty() == False:
        boardinglist.append(reg.dequeue())
    
    return(boardinglist)

print(split(line))

print(board(regularQ,preQ)) 

#%%
from IPython import get_ipython
get_ipython().magic('reset -sf')

from QueueClass import *

stockQ = Queue()

for i in range(50):
    stockQ.enqueue(20)
    
for i in range(50):
    stockQ.enqueue(22)

for i in range(50):
    stockQ.enqueue(25)

print(stockQ.size())


def sell(bought):
    
