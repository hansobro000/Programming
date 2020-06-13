# -*- coding: utf-8 -*-
"""
Created on Tue May  5 20:44:39 2020

@author: Brooks Hanson
"""

#%%
#Write a function which will find all such numbers which are divisible by 7 
#but are not a multiple of 5,between 2000 and 3200 (both included). 
#The numbers obtained should be printed as a list.

lst = []

for i in range(2000,3201):
    if i % 7 == 0 and i % 5 != 0:
        lst.append(i)

print(lst)
#%%

#Write a function which can compute the factorial of a given number.
number = int(input("Enter number for factorial calculation: "))

def factorial(number):
    if number == 0:
        return 1
    #recursion to get to base case
    else:
        return (number * factorial(number-1))

print(factorial(number))
#%%
#Define a class which has at least two methods: getString: to get a string 
#from console input printString: to print the string in all upper case. 
#Also please include a simple test function to test the class methods.

class StringStuff:
    def __init__(self):
        self.got = self
    
    def getString(self):
        mySTR = str(input("Enter string: "))
        self.got = mySTR
    
    def printString(self):
        upper = self.got.upper()
        return(upper)

def test():
    m = StringStuff()
    m.getString()
    print(m.printString())

test()
#%%
#Write a function that accepts a sequence of whitespace separated words as 
#input and prints the words after removing all duplicate words and sorting 
#them alphanumerically. Words should be printed as a list.Suppose the 
#following input is supplied to the functionhello world and practice makes 
#perfect and hello world againThen, the output should be:again and hello makes 
#perfect practice world

def whitespace():
    s = input('Enter words split by spaces ')
    
    words = [word for word in s.split(" ")]
    
    st = set(words)
    
    l = list(st)
    
    l.sort()
    
    print(l)

whitespace()
#%%
#Write a function which will find all such numbers between 1000 and 3000 
#(both included) such that each digit of the number is an even number.
#The numbers obtained should be printed as a list.

def evenDigitNums():     
    values = []
    for i in range(1000, 3001):
        s = str(i)
        if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
            values.append(s)
            print(values)

evenDigitNums()        
#%%
#Define a triangle class. Create a constructor and a method that returns 
#the area of the triangle. Also please include a simple test function to 
#test the class methods.  Area of a triangle = base * height /2

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        area = self.base * self.height / 2
        return(area)

U = Triangle(3,4)
str(U)
def testT(b,h):
    m = Triangle(b,h)
    print(m.area())

testT(3,9)

#%%