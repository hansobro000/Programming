# Homework problems for chapters 6 and 7.

# Chapter 6 exercise 5:

# This program simplifies the previous cost per square inch of pizza program
# through the use of functions. The radius of the pizza is entered into the 
# function area and the price of the pizza is entered into the function costP
# witch then uses the area function to calcualte the cost per square inch
# of pizza.

import math

def area(radius):
    return math.pi * math.pow(radius,2)

def costP(price):
    costP = price/area(8)
    print("The cost per square inch of your pizza is: $"+str(round(costP,2)))

costP(25)

print()

# logic is correct, but assumes a pizza that is 8" in diameter (hard coded in the costP function)

# Chapter 6 exercise 9:

# This program simplifies the previous letter grade program through the
# use of functions. Entering the score you recieved in the finction grade 
# will return the cooresponding letter grade.

def grade(score):
    if score >=90:
        print("Your grade is an 'A'")
    if 90> score >=80:
        print("Your grade is a 'B'")
    if 80> score >=70:
        print("Your grade is a 'C'")
    if 70> score >=60:
        print("Your grade is a 'D'")
    if score <60:
        print("Your grade is an 'F'")

grade(50)

# good

print()

# Chapter 7 exercise 5:

# This program calcualtes your Body Max Index based on your given height and
# weight, and determines if it is above, below, or within a healthy range.

import math

def BMI():
    lbs, inches = eval(input("Please enter your weight followed by hight in inches; separated by a comma. "))
    bmi = lbs * 720 / math.pow(inches, 2)
    if bmi > 25:
        print("At a BMI of ", round(bmi, 2), ", you are above the healthy range of 19-25.")
    elif bmi < 19:
        print("At a BMI of ", round(bmi, 2), ", you are below the healthy range of 19-25.")
    else:
        print("At a BMI of ", round(bmi, 2), ", you fall within the healthy range of 19-25.")

BMI()

print()

# good

# Chapter 7 exercise 7:

# This program will calculate the total earnings from a babysitting job
# acrosse two different pay rates based on when you worked.

def main():
    start = float(input("What time did you start (in military notation)? "))
    end = float(input("When did you end (in military notation)? "))
    if end <= 21:
        bill = (end - start) * 2.5
        print("Your bill is: $"+str(round(bill,2)))
    elif end > 21:
        bill = ((end - 21) * 1.75) + ((21 - start) * 2.5)
        print("your bill is: $"+str(round(bill,2)))
    else:
        print("We fucked up")
        
main()

print()

# works if time is entered in only hours
#if you entere minutes in military time format (12:30) the program crashes
# users would have to convert to a time with a decimal. instead of 12:30 you'd
# have to enter 12.5

# Chapter 7 exercise 9:

# This program will accurately predict when easter will fall or did fall in 
# any year since 1982 and until the year 2048

def main():
    year = int(input("For what year would you like to know when Easter is? "))
    a = year%19
    b = year%4
    c = year%7
    d = (19 * a + 24)%30
    e = (2 * b + 4 * c + 6 * d +5)%7
    # easter = march 22 + d + e
    
    if year >=1982 and year <=2048:
        easter = 22 + d + e
        if easter > 31:
            easter = easter - 31
            print("Easter falls on April", easter, year)
        else:
            print("Easter falls on March", easter, year)
    else:
        print("You did not enter a year that falls within our range. Please try again with a valid year")

main()

print()

# I messed up and did exercise 9 instead of exercise 12 when I first submitted
# so here is chapter 7 exercise 12 as well:

# This program evaluates the day, month, and year entered,and determines if 
# it is a valid year, then a valid month, then a valid day by using
# if-else and if-elif-else rules.

def main():
    year = int(input("Enter the year: "))
    month = int(input("Enter the month: "))
    day = int(input("Enter the day: "))
    
    if year >= 1:
        print("Valid year.")
        if month >= 1 and month <= 12:
            print("Valid month.")
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 12:
                if day >= 1 and day <= 31:
                    print("Valid day.")
                else:
                    print("Invalid day.")
            elif month == 4 or month == 6 or month == 9 or month == 11:
                if day <= 30 and day >= 1:
                    print("Valid day.")
                else:
                    print("Invalid day.")
            elif month == 2:
                if day <= 28 and day >= 1:
                    print("Valdi day.")
                else:
                    print("Invalid day.")
        else:
            print("Invalid month.")
    else:
        print("Invalid year.")
        
main()

# good
