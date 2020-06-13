# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 23:10:32 2019

@author: brook
"""
#%%

# Chapter 8 Exercise 1

# This program finds the n'th number of Fibonacci

def main():
    F = 0
    new = 1
    count = 0
    n = int(input("Which Fibonacci number would you like to know? "))
    while count <= n - 1:
        new = new + F
        F = new - F
        count = count + 1
    print(F)
    
main()

# good

#%%

# Chapter 8 Exercise 3

# This program calculates the amount of time it will tkae to double your 
# investment based on the interest rate provided.

def main():
    amount = float(input("What is the starting amount of your investment? "))
    IR = float(input("What is the annual interest rate? "))
    year = 0
    double = amount * 2
    while amount <= double:
        amount = amount * (1 + (IR / 100))
        year = year + 1
    
    print("\nYour investment will double to ${:,.2f}".format(double),"in "+str(year)+" years")
    
main()

#good
#%%

# Chapter 8 Exercise 4

# This program displays the Syracuse sequence for the natural number entered.
# Error checking is also used to make sure the number entered is 
# actually a natural number.

def main():
    while True:
        try:
            x = int(input("Enter a natural number: "))
            if x >= 0:
                break
            else:
                print("The number you entered was not a natural number")
        except ValueError:
            print("The number you entered is not a natural number")
    
    print("\nThe Syracuse sequence starting with", x, "is: ")
    print(x)
    while x >= 1:
        if x == 1:
            break
        elif x % 2 == 0:
            x = x / 2
            print(int(x))
        elif x % 2 != 0:
            x = (3 * x) + 1
            print(int(x))
        

main()

# not assigned
#%