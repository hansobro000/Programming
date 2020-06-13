# HW 2

# This is a program that calculates the cost per square inch of a circular
# pizza, given its diameter and price

import math

def main():
    diameter = float(input("Enter the diameter of your pizza (in inches): "))
    price = float(input("Enter the price you paid for your pizza (in USD): "))
    
    radius = diameter / 2
    area = math.pi * math.pow(radius,2)
    
    costP = price / area
    
    print("\nThe cost per square inch of your pizza is: $"+str(round(costP,2)))
    
main()

# good

print()

# This program calculates the cost of your order of coffe

def main1():
    print("The total cost of your order includes shipping \n")
    
    lbs = float(input("How many pounds of coffee are you purchasing? "))
    sellP = lbs * 10.50
    shipping = lbs * 0.86 +1.5
    
    total = sellP + shipping
    
    print("\nYour order total is: $"+str(round(total,2)))

main1()

# good

print()


# This program gives the results of x^y

def main2():
    
    inputs = input("Please enter your x and y values in x,y format: ").split(",")
    x,y = float(inputs[0]), float(inputs[1])
    
    output = int(math.pow(x,y))
    
    print("Your result is: ", output)

main2()

# good

print()

# This program calcualtes the expected revenue of the bike shop given
# the number of bikes they expect to sell

def main3():
    
    print("\nAt Brooks' Bike Shop we found out the hiden formula for predicting next months revenue. ")
    print("\nAll we have to do is figure out how many bikes we are going to sell!")
    
    bikes = int(input("How many bikes do you think we will sell at Brooks' Bike Shop next month? "))
    helmets = int(bikes / 5)
    revenue = (bikes * 250) + (helmets * 50)
    
    print("\nNext months revenue will be $"+str(round(revenue,2)), "if we follow")
    print("through and sell our expected", bikes, "bikes.")
    
main3()

# good

print()

# This program acts as a word counter

def main4():
    
    sentence = str(input("Please enter your sentence or phrase: "))
    
    sentence = sentence.split( )
    
    print("\nYour sentence has", len(sentence), "words")
    
main4()

# good

print()
