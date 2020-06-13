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
#   also, functions inside classes. use dot notation

#%%

myStr = 'Hello World'
dir(myStr)

myList = [1,2,3,4,5]
dir(myList)

#%%

# Define a class
# Think of a class as a blueprint

class Fraction:
    pass

myFraction = Fraction()
print(dir(myFraction))
#%%

myF = Fraction()

print(myF)

#%%

anotherF = Fraction()
print(anotherF)
print(myF)

#%%
# The init method
# set up all the initial states for the object
# called a "constructor"

class Fraction:
    def __init__(self,numerator,denominator):
        self.num = numerator
        self.den = denominator
# self operator shows that the variable we want to use takes the place
# of self. Keeps track of what variable we are using

myFraction = Fraction(1,2)
print(dir(myFraction))
#%%

myf = Fraction(3,4)

anotherf = Fraction(5,6)

print(myf.num)
print(myf.den)

print(anotherf.num)
print(anotherf.den)

#%%

# it would be easier to print in a format we recognize - num/den

class Fraction:
    def __init__(self,numerator,denominator):
        self.num = numerator
        self.den = denominator
        
    def show(self):
        print(str(self.num) + '/' + str(self.den))
        
myf = Fraction(3,4)
myf.show()

print(myf)
print(dir(myf))

#%%

# wouldnt it be easier if we could just use the standard print function?
# were foing to override the __str__ function

class Fraction:
    def __init__(self,numerator,denominator):
        self.num = numerator
        self.den = denominator
        
    def __str__(self):
        return(str(self.num) + '/' + str(self.den))
    
# __str__ is the built in print function. Overriding it basically turns
# the attribute of our class into a str that the print funtion can use
    
myf = Fraction(3,4)
print(myf)

#%%

myF = Fraction(1,2)
myF2 = Fraction(2,4)

# are the above fractions equal?

myF == myF2

# just like the print/show methods, this class doesnt let 
# you do comparisons yet

#%%
# cross multiplication to overide the equal method
class Fraction:
    def __init__(self,numerator,denominator):
        self.num = numerator
        self.den = denominator
        
    def __str__(self):
        return(str(self.num) + '/' + str(self.den))
    
    def __eq__(self,fraction2): # __eq__(self,other) so we are just naming other 'fraction2'
        firstNum = self.num * fraction2.den
        secondNum = fraction2.num * self.den
        return(firstNum == secondNum)

myF = Fraction(1,2)
myF2 = Fraction(2,4)

myF == myF2

#%%
# override the __add__ method

class Fraction:
    def __init__(self,numerator,denominator):
        self.num = numerator
        self.den = denominator
        
    def __str__(self):
        return(str(self.num) + '/' + str(self.den))
    
    def __eq__(self,fraction2):
        firstNum = self.num * fraction2.den
        secondNum = fraction2.num * self.den
        return(firstNum == secondNum)
    
    def __add__(self,fraction2):
        newNum = self.num*fraction2.den + fraction2.num*self.den
        newDen = self.den * fraction2.den
        newF = Fraction(newNum,newDen)
        return(newF)
        # make sure you return the right type
    
myF = Fraction(1,2)
myF2 = Fraction(1,4)

print(myF + myF2)

#%%
# we usually reduce fractions. Euqlid has an option.
# we find the greatest common devisor and we'll use
# that to reduce our fraction.

def gcd(int1,int2):     # euclids algorithm
    while int1%int2 != 0:
        oldInt1 = int1
        oldInt2 = int2
        int1 = oldInt2
        int2 = oldInt1%oldInt2
    return(int2)

#%%
# so this is what we end up with:
    
class Fraction:
    def __init__(self,numerator,denominator):
        self.num = numerator
        self.den = denominator
        
    def __str__(self):
        return(str(self.num) + '/' + str(self.den))
    
    def __eq__(self,fraction2):
        firstNum = self.num * fraction2.den
        secondNum = fraction2.num * self.den
        return(firstNum == secondNum)
    
    def __add__(self,fraction2):
        newNum = self.num*fraction2.den + fraction2.num*self.den
        newDen = self.den * fraction2.den
        commonDen = gcd(newNum,newDen)
        return(Fraction(newNum // commonDen,newDen // commonDen))

def gcd(int1,int2):     # euclids algorithm
    while int1%int2 != 0:
        oldInt1 = int1
        oldInt2 = int2
        int1 = oldInt2
        int2 = oldInt1%oldInt2
    return(int2)
    
myF = Fraction(1,2)
myF2 = Fraction(1,4)

print(myF + myF2)
print(myF == myF2)


#%%
# Heinrich's Fraction Class:

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
    return(int2) # if return statement is indented one further, inside
                # the while loop, and the condition isnt met, then
                # we will never reach the return statemnt
        

myFraction = Fraction(1,4)
myFraction2 = Fraction(1,2)

print(dir(myFraction))
print(myFraction)

print(myFraction + myFraction2)

print(myFraction == myFraction2)

#%%

class Vehicle:
    
    def __init__(self,Mk,Mdl,Clr):
        self.Make = Mk
        self.Model = Mdl
        self.Color = Clr
        
    def show(self):
        return(str(self.Make) + str(self.Model))
    
    def __str__(self):
        return(str(self.Color) + " " + str(self.Make) + " " +  str(self.Model))
    
    def colorChange(self, newColor):
        self.Color = newColor

Car1 = Vehicle("Chevrolet","Suburban","White")
Car2 = Vehicle("Ford","F-150","Blue")    
Car3 = Vehicle("Dodge","Ram 1500","Black")
Car4 = Vehicle("Toyota","Camrey","Silver")

print(Car1.show())

print(Car2)

Car1.colorChange("YASSSS")
print(Car1)



#%%
# Example of Paul's error

def foo(p1,p2):
    if p1 > p2:
        return(True)
    return() # this is the key that he needed. condition isnt met, still
                # return

a = 3
b = 2

print(foo(a,b))

c = 4
d = 5

print(foo(c,d))





