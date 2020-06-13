# Homework assignment 1.

#This is a program that calculates and displays a players batting average
#Enter the player's name including " 's " into name()

def name(player):
    x = eval(input("Enter number of hits: "))        
    y = eval(input("Enter number of at-bats: ")) 
    
    print("What is the player's name?", player)
    print("How many hits?", x)
    print("How many at-bats?", y)
    print(player,"'s batting average is", x / y)
    
name("Jorge Polanco")

# Function should prompt for the players name
# 8/10


print()
print()


#This is a program that creates a list of my favorite foods
        
def list():
    print("My favorite foods are:")
    for food in ["Cheesecake", "Sushi", "Ice cream", "Steak"]:
        print(food)
list()

# good, but be careful. list() is actually a reserved word that converts
# a variable into a list type or creates a new list object. 
# You've overridden the default use of list()
# by creating your own function called list().  Notice that list is actually
# colored red by default, indicating it's a reserved word.

# https://www.programiz.com/python-programming/methods/built-in/list

# no way you could have known this at this initial level, but wanted to point
# out the potential problem here. Python actually lets you redefine everything
# but not necessarily recommended.

# 10/10

print()
print()


# This program takes words entered as promted and creates a sentence out of them.

def sentence():
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adj = input("Enter an adjective: ")
    plc = input("Enter a place: ")

    print("Take your", adj, noun, "and", verb, "it at the", plc, "!")
    
sentence()

# good 10/10


print()
print()


#This program takes the sum of two numbers that are simultaniously assigned.

def addition():
    print("This program takes the sum of two numbers together.")
    
    var1, var2 = eval(input("Enter two numbers separated by a comma: "))
    sum = (var1 + var2)
    
    print("The sum of your numbers is: ", sum)
    
addition()

# good 10/10

print()
print()


# This is a program that prints 10,000 consecutive numbers AND adds 1 to each number

def loop():
    for i in range(10000):
        print(i, (i +1))

loop()

# good 10/10
