# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 11:20:09 2018

@author: matth
"""

#basic function stuff

def myFunction(parm1, parm2):
    print("this is parm1 " + parm1)
    print("this is parm2 " + parm2)
    return()
    


myFunction("Hello", "World")
myFunction("hello")

#%%
#pass values for specific parameters

myFunction(parm2 = "World", parm1 = "Hello")

#%%
# bad parameters

myFunction("Hello")

myFunction(1,2)


#%%
#Optional parameter with default

def myFunction2(parm1, parm2 = "World"):
    print("this is parm1 " + parm1)
    print("this is parm2 " + parm2)
    return()
    
myFunction2("Hello")
myFunction2("Hello", "Idiot")

#%%
#returning values

def conCat(firstName="", lastName=""):
    returnValue = lastName + ", "+ firstName
    return(returnValue)

name = conCat("Matt", "Heinrich")
print(name)   
# Function takes on the value of the stuff done inside the function 

print(conCat("Matt", "Heinrich"))

strng1 = conCat("Matt", "Heinrich")
print(strng1)

#%%

#simple algorithm for finding a prime number.

def isPrime(x):
    if x > 0:
        for i in range(2,x):
            if (x % i) == 0:
                return(False)
        return(True)
    else:
        return(False)
        
        
userVal = int(input("Enter a whole number: "))

if isPrime(userVal):
    print(str(userVal) + " is a prime number.")
else:
    print(str(userVal) + " is not a prime number.")


#%%
#Variable scope
# gVariable is defined "outside" or globally and it's still 
# available inside the function foo

gVariable = "Hello World"

def foo():
    print("Inside function foo. gVariable = " + gVariable)
    
print("Outside of function foo. gVariable = " + gVariable)
foo()




#%%
# the myVar inside changeVar is actually a different variable.
# it is not the same as the global assignmnet and therefore
# you're not changing it inside the function changeVar

myVar = "Global Assignment"

def changeVar():
    myVar = "Local Assignment"
    print(myVar)
    return()
    
print("Before function " + myVar)
changeVar()
print("After function " + myVar)

#%% 
#variable scope with global identifier
# twist on the above. We're referring to the global variable myVar
# by using a special keyword "global". this actually allows us to 
# change the global variable within our function changeVar


myVar = "Global Assignment"

def changeVar():
    global myVar
    myVar = "Local Assignment"
    print("In function changeVar() " + myVar)
    return()
    
print("Before function " + myVar)
changeVar()
print("After function " + myVar)


#%%

#lists assignments are immutable

myGlobalList = [1,2,3,4]

def changeList(l):
    l = [97,98,99]
    return()
    

print("Before function ")
print(myGlobalList)
changeList(myGlobalList)
print("After function ")
print(myGlobalList)

#%%

# list items are not immutable
# can be confusing until you get used to it.

myGlobalList = [1,2,3,4]
def changeListItem(l):
    #l = [40,50,60]
    l[0] = 97
    l[1] = 98
    l[2] = 99
    
print("Before function ")
print(myGlobalList)
changeListItem(myGlobalList)
print("After function ")
print(myGlobalList)

#%%
#the print functions here don't actually print the values of
# the list items. It prints the address in memory of where the 
# list items are stored. Still somewhat confusing, but might
# give a better understanding of why the individual elements can
# be changed.


myGlobalList = [1,2,3,4]
print(id(myGlobalList))
print(id(myGlobalList[0]))
print(id(myGlobalList[1]))
print(id(myGlobalList[2]))
print(id(myGlobalList[3]))
print(myGlobalList)

changeListItem(myGlobalList)
print(id(myGlobalList))
print(id(myGlobalList[0]))
print(id(myGlobalList[1]))
print(id(myGlobalList[2]))
print(id(myGlobalList[3]))
print(myGlobalList)
    
#%%

#demonstration of a useful algorithm. newtons method for approximating
# a square root

# This uses a relatively brute force method for x in range(20) to 
# get to the return value. This algorithm usually converges in 5 
# iterations to 10 decimal places so probably not necessary to go
# that far. Can we make the algorithm "better"?

def squareRoot(x):
    root = x/2
    for y in range(20):
        root = (.5*(root+x/root))
    return(root)
    
    
squareRoot(145)

#%%
# original version
# the for loop is always going to execute 20 times

def squareRoot(x):
    root = x/2
    for y in range(20):
        root = (.5*(root+x/root))
    return(root)

#%%

# let's change the function to stop after getting "close enough"
# in this example, 10 decimal places is close enough.    
    
def squareRoot2(x):
    closeEnough = 0.0000000001
    counter = 0
    root = x/2
    
#multiply our square root guess by itself and subtract the 
#original number. If we're not close enough, continue to iterate
# through the while loop.    
    while root * root - x > closeEnough:
        root = (.5*(root+x/root))
        counter = counter + 1
        
        
    print("Final counter " + str(counter))    
    return(root)
    
print(squareRoot(145))
print(squareRoot2(145))
    
    