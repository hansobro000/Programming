# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 14:12:29 2020

@author: Brooks Hanson
"""

#%%
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 18:43:55 2019

@author: matth
"""
#%%

#reset environment
from IPython import get_ipython
get_ipython().magic('reset -sf')

from StackClass import *
#%%

def parChecker2(symbolString):

    s = Stack()

    balanced = True
    index = 0

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        elif symbol in ")]}":
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                       balanced = False

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = "([{"
    closers = ")]}"

    return opens.index(open) == closers.index(close)


#%%
    
parChecker2('{([])}')
parChecker2('{b}')
parChecker2('{[{}}')
parChecker2('([)]')
