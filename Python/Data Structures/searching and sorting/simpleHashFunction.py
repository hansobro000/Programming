# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 15:08:20 2020

@author: Brooks Hanson
"""
#%%

tblSize = 41
# modulus tablesize for range of 0-40

# simple hash of first character of string passed in
def calcHash1(inval):    
    return(ord(inval[0])%tblSize)

# add all the ordinal values of the characters of the passed in string
def calcHash2(inval):
    retval = 0    
    for x in inval:        
        retval = retval + ord(x)    
    return(retval%tblSize)

# add all the ordinal values of the characters passed in offset by 128
def calcHash3(inval):    
    retval = 0    
    for x in inval:        
        retval = 128*retval + ord(x)    
        return(retval%tblSize)
    
#%%
        
#usage would be

calcHash1('MattHeinrich')

# I omitted spaces in my example, but not strictly required. Spaces are ord 32.

#%%