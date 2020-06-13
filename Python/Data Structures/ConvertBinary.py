# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 14:24:22 2020

@author: Brooks Hanson
"""

#%%
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 18:50:24 2019

@author: matth
"""
#%%

#reset environment
from IPython import get_ipython
get_ipython().magic('reset -sf')

from StackClass import *
#%%

def divideBy2(decNumber):

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString
#%%
    
print(divideBy2(8))