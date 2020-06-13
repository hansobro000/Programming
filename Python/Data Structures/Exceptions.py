# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 08:31:09 2018

@author: matth
"""
#%%
#Exception Handling

x = 5
myString = "Hello World"

print(myString + x)

#Doesn't know or try to convert the integer to a string.

#%%

# With exception handling

x = 5
myString = "Hello World"

try:
    print(myString + x)
except:
    print("Something went wrong.")
    
#%%


x = 5
myString = "Hello World"

try:
    print(myString + x)
except TypeError:
    print("Something went wrong. Data Type Error")
except ValueError:
    print("Something went wrong. Data Value Error")    
    
#%%
    
try:
    y = int(input("Enter a number."))
except TypeError:
    print("Something went wrong. Data Type Error")
except ValueError:
    print("Something went wrong. Data Value Error")    
    
    
    
#%%
    
#raising our own exception


x = 5
myString = "Hello World"

if isinstance(myString,str) != True:
    raise ValueError("Invalid value for myString passed.")
if isinstance(x,str) != True:
    raise ValueError("Invalid value for x passed.")
    
print(myString+x)
    