# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 13:15:04 2020

@author: Brooks Hanson
"""

#%%
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 17:57:42 2019

@author: matth
"""

#%%
#iteration

def listsum(l):
    retval = 0
    for i in l:
        retval = retval + i
    return(retval)

#%%

#recursion
    
def recSum(l):    
    if len(l) == 1:
        return(l[0])
    else:
        return(l[0]+recSum(l[1:]))



#%%

x = [1,2,3,4]
print(listsum(x))

print(recSum(x))


#%%
convertString = '0123456789ABCDEF'

def toStr(n,base):
    if n < base:
        return(convertString[n])
    else:
        return(toStr(n//base,base) + convertString[n % base])  
        
        
#%%

print(toStr(10,2))
print( toStr(123454,16))


print(isinstance(toStr(12345,10),str))
        
#%%

from StackClass import *

convertString = '0123456789ABCDEF'

rstack = Stack()

def toStrStack(n, base):
    if n < base:
        rstack.push(convertString[n])
    else:
        rstack.push(convertString[n % base])
        toStrStack(n//base,base)


toStrStack(10,2)

strng = ''
while not rstack.isEmpty():
    strng = strng + rstack.pop()

print(strng)

#%%        



#%%
