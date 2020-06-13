# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 09:04:33 2018

@author: matth
"""

#%%

#For loops

# range ([start,] stop [,increment])


for x in range(5):
    print(x)

#%%
   
for x in range(1,4):
    print(x)

print("*****************")

for x in range(1,4,2):
    print(x)

print("*****************")

for x in range(100,0,-20):
    print(x)

# Can decrimant but since it is the end spot, doesn't include end

#%%
# List is collection 
myList = ["Calculus","Physics","Programming","Statistics"]

for x in myList:
    print("this is x now " + x)
    
#%%    
# String is also a collection
myStrng = "Hello World"
for x in myStrng:
    print(x)
 
#%%    
# Basically rows and collumns in a spreadsheet
for x in myList:
    print(x)
    for y in x:
        print(y)

#%%


for x in reversed(myList):
    print("This is x now " + x)    

# Same thing but slicing. Iterating from the end    
for x in myList[::-1]:
    print(x)
    
# Specify start and stop
for x in myList[len(myList)-1::-1]:
    print(x)
    
    
#%%
#While Loops --- Infinite, must tell it to end    


x = 0
while x < 10:
    print(x)
    x = x + 1

print("********************")

x = 0
while x < 10:
    print(x)
    x += 2  #sames as x = x + 2
#%%
 
    
while True:
    x = float(input("Enter an even whole number "))
    if x % 2 == 0:
        print("Well done ")
    else: 
        print("I said an even whole number you moron ")
        break

#%%
# Example of a web form
        
print("Enter yoour text - enter 'qq' to stop")
textStr = ""  
  
while x != "qq":
    x = input()
    if x != "qq":
        textStr = textStr + x
        
print(textStr)
    
        
#%%
# Accumulator. Keeps track of the numbers entered. if new number is 
# larger than old number, it gets replaced by new. When done, prints 
# largest number

maxValue = 0

print("enter 'done' to print the largest value")

while True:
    x = input("Enter a number ")
    if x == 'done':
        break
    x = float(x)
    if x > maxValue:
        maxValue = x

print("The maximum number entered was " + str(maxValue))        

#%%
#Unpacking

nameList = [["CS","Computer Science"],["MT","Math"],["PY","Psychology"],["AC","Accounting"]]
for abrev,title in nameList:
    print(abrev,title)

#%%
# Practice2

evenNumbers = list(range(0,100,2))
print(evenNumbers)

oddNumbers = tuple(range(1,100,2))   
print(oddNumbers)

s = set(['A','B','C','D','A','A','B'])
print(s)
# B, D, A, C

oddSet = set(range(1,100,2))    
print(oddSet)
divFiveSet = set(range(0,100,5))
print(divFiveSet)

print(oddSet & divFiveSet)


ALCentral = {"Chicago":"White Sox","Cleveland":"Indians","Detroit":"Tigers","Kansas City":"Royals","Minnesota":"Twins"}
print(ALCentral["Detroit"])
