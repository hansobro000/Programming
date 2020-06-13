# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 08:22:08 2018

@author: matth
"""

#%%
#if else statements


x = 8
y = 6
z = 5

# Indentation is the begin and end. Everything on the same level 
# will run.

if x > y:
    print("X is larger than y")
    
if y > z:
    print("Y is larger than z")
else:
    print("Z is larger than or equal to y")
    
 
#%%
def main():
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    z = int(input("Enter z: "))

# which is largest

    if x >= y and x >= z:
        print("x is largest")
    elif y >=x and y >= z:
        print("y is largest")
    else:
        print("z is largest")

main()

    
#%%

x = int(input("Enter x "))
y = int(input("Enter y "))
z = int(input("Enter z "))
    
if x >= y:
    if x >=z:
        print("x is largest")
    elif z >= y:
        print("z is largest")
elif y >= z:
    print("y is largest")
elif z >= x:
    if z >= y:
        print("z is largest")

#%%
        
x = input("Enter x ")
y = input("Enter y ")
z = input("Enter z ")

if x >= y:
    if x >= z:
        print("x is largest")
    else:
        print("z is largest")
else:
    if y >=z:
        print("y is largest")
    else:
        print("z is largest")
        
    
#%%

# This is looping through the dataset and assigning the max value so far
# to x and checking against it.

x = input("Enter x ")
y = input("Enter y ")
z = input("Enter z ")

strng = "x is largest"
maxvalue = x

if y > x:
    maxvalue = y
    strng = "y is largest"
if z > maxvalue:
    maxvalue = z
    strng = "z is largest"
    
print(str(maxvalue) + ", " + strng)
    

               