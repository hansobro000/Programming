# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 13:37:33 2020

@author: Brooks Hanson
"""

#%%
#1
def largest(x,y,z):
    #Use modular division to check if parameters are
    #not integers. If any of
    #these cases are true, or the inputs are a string, the
    #corresponding error will be raised. 
    go = True
    try:
        if x%1 != 0 or y%1 != 0 or z%1 != 0:  
            raise TypeError
    except (TypeError,ValueError):
        print("Integers only dude")
        go = False
    #If no errors are raised, then it must be 
    #integer components, and the parameters can be initialized.
    if go:
        maxvalue = x
        if y > x:
            maxvalue = y
        if z > maxvalue:
            maxvalue = z
            
        return(maxvalue)

#%%
#2
def odd():
    oddlist = []
    for x in range(1,50,2):
        oddlist.append(x)
    return(oddlist)

odd()

#%%
#3

def PrimeList():
    plist = []
      
    for val in range(2, 50): 
       
    # If num is divisible by any number   
    # between 2 and val, it is not prime  
        for n in range(2, val): 
            if (val % n) == 0: 
                break
        else: 
            plist.append(val)
    return(plist)
                
PrimeList()
#%%

for x in range(3):
    print(x)