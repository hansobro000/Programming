# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 13:35:23 2020

@author: Brooks Hanson
"""

#%%
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 19:34:19 2019

@author: matth
"""
#%%
#reset environment
from IPython import get_ipython
get_ipython().magic('reset -sf')

from QueueClass import *



#%%


def circularQue(namelist, N):

    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(N):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()
#%%
    
l = ['Matt','Lisa','Scott','Ian','Joe','Floof','Butthead', 'Fishy']

remain = circularQue(l,4)
print(remain)