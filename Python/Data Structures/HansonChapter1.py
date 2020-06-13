# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 20:21:44 2020

@author: Brooks Hanson
"""

class Fraction:
    def __init__(self,numerator,denominator):
        #Use modular division to check if numerator or denominator are
        #not integers. Then check if the denominator is zero. If any of
        #these cases are true, or the inputs are a string, the
        #corresponding error will be raised. 
        try:
            if numerator%1 != 0 or denominator%1 != 0:  
                raise TypeError
            if denominator == 0:
                raise ZeroDivisionError
        except (TypeError,ValueError,ZeroDivisionError):
            print("Integers only dude")
        #If no errors are raised, then it must be a fraction containing
        #integer components, and the parameters can be initialized.
        else:
            commonDen = gcd(numerator,denominator)
            num = numerator // commonDen
            den = denominator // commonDen
            #Using Euclids algorithm, the greatest common divisor is 
            #found to simplify the fraction.
            self.num = num
            self.den = den

    def __str__(self):
        #Convert numerator and denominator into string form so print
        #function can recognize fraction class.
        return(str(self.num) + '/' + str(self.den))
    
    def __eq__(self,fraction2):
        #multiply numerators by other denominators. Use built in == 
        #to get boolean output testing equality.
        firstNum = self.num * fraction2.den
        secondNum = fraction2.num * self.den
        return(firstNum == secondNum)
    
    def __add__(self,fraction2):
        #Cross multiplication to add two fractions
        newNum = self.num*fraction2.den + fraction2.num*self.den
        newDen = self.den * fraction2.den
        #convert outputs to fraction class
        return(Fraction(newNum,newDen))
    
    def __sub__(self,fraction2):
        #Cross multiplication to subtract two fractions
        newNum = self.num*fraction2.den - fraction2.num*self.den
        newDen = self.den * fraction2.den
        #convert outputs to fraction class
        return(Fraction(newNum,newDen))
    
    def __mul__(self,fraction2):
        #multiply two fractions
        newNum = self.num * fraction2.num
        newDen = self.den * fraction2.den
        #convert outputs to fraction class
        return(Fraction(newNum,newDen))
    
    def __truediv__(self,fraction2):
        #Multiply first fraction by inverse of second fraction to 
        #do true division on two fractions.
        newNum = self.num * fraction2.den
        newDen = self.den * fraction2.num
        #convert outputs to fraction class
        return(Fraction(newNum,newDen))
    
    def __gt__(self,fraction2):
        #multiply numerators by other denominators. Use built in > 
        #to get boolean output testing greater than.
        firstNum = self.num * fraction2.den
        secondNum = fraction2.num * self.den
        return(firstNum > secondNum)
    
    def __ge__(self,fraction2):
        #multiply numerators by other denominators. Use built in >= 
        #to get boolean output testing greater than or equal to.
        firstNum = self.num * fraction2.den
        secondNum = fraction2.num * self.den
        return(firstNum >= secondNum)
    
    def __lt__(self,fraction2):
        #multiply numerators by other denominators. Use built in < 
        #to get boolean output testing less than.
        firstNum = self.num * fraction2.den
        secondNum = fraction2.num * self.den
        return(firstNum < secondNum)
    
    def __le__(self,fraction2):
        #multiply numerators by other denominators. Use built in <= 
        #to get boolean output testing less than or equal to.
        firstNum = self.num * fraction2.den
        secondNum = fraction2.num * self.den
        return(firstNum <= secondNum)
    
    def __ne__(self,fraction2):
        #multiply numerators by other denominators. Use built in != 
        #to get boolean output testing inequality.
        firstNum = self.num * fraction2.den
        secondNum = fraction2.num * self.den
        return(firstNum != secondNum)

def gcd(int1,int2):     # euclids algorithm
    while int1%int2 != 0:
        oldInt1 = int1
        oldInt2 = int2
        int1 = oldInt2
        int2 = oldInt1%oldInt2
    return(int2)
