# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 13:25:11 2020

@author: Brooks Hanson
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 09:44:54 2018

@author: matth
"""
#%%

# Attributes - Stuff we know
# Methods - Stuff we do

#%%

myStr = 'Hello World'
dir(myStr)

#%%

# Define a class
# Think of a class as a blueprint

class Fraction:
    
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom
    
    def __str__(self):
        return(str(self.num) + "/" + str(self.den))
    
    def __add__(self,fraction2):
        newNum = self.num*fraction2.den + fraction2.num*self.den
        newDen = self.den * fraction2.den
        commonDen = gcd(newNum,newDen)
        return(Fraction(newNum // commonDen,newDen // commonDen))

    def __eq__(self,fraction2):
        firstNum = self.num * fraction2.den
        secondNum = fraction2.num * self.den
        return(firstNum == secondNum)

def gcd(int1,int2):     # euclids algorithm
    while int1%int2 != 0:
        oldInt1 = int1
        oldInt2 = int2
        int1 = oldInt2
        int2 = oldInt1%oldInt2
    return(int2)
        

myFraction = Fraction(1,4)
myFraction2 = Fraction(1,2)

print(dir(myFraction))
print(myFraction)

print(myFraction + myFraction2)

print(myFraction == myFraction2)