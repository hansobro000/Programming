# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 13:56:40 2020

@author: Brooks Hanson
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 18:33:34 2019

@author: matth
"""

#%%

#reset environment
from IPython import get_ipython
get_ipython().magic('reset -sf')

from StackClass import *
#%%


def parChecker(symbolString):
    s = Stack()

    balanced = True
    index = 0

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        elif symbol == ")": 
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

#%%
    
parChecker("(d)")    
parChecker("(()")
parChecker(")))asdf(((")
parChecker("asdf")
