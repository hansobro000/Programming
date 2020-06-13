# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 13:40:53 2020

@author: Brooks Hanson
"""

#%% #1
def NFactorial(n):
    #base case
    if n == 0:
        return 1
    #recursion to get to base case
    else:
        return (n * NFactorial(n-1))

#%% #2
def RevList(lst):
    #base case
    if len(lst) < 2:
        #if list is length 0 or 1, reversing is redundant, so empty/existing 
        #list is returned
        return lst
    #recursion to get to base case
    else:
        return (RevList(lst[1:]) + [lst[0]])

#%% #5
#recursive
def FibR(f):
    #base case
    if f <= 1:
        #the 0th fib num is 0, and the 1st fib num is 1, so f is the desired num
        return f
    #recursion to get to base case
    else:
        #this recursion follows the mathematical formula of Xn = Xn-1 + Xn-2
        return (FibR(f-1) + FibR(f-2))

#iterative
def fibI(f):
    #assign a = 1 and b = 2. the 0th and 1st numbers in the sequence
    a,b = 0,1
    #iterate through each number up to the number we wish to find
    for i in range(f):
        #assign next a to current b, and b to current a plus current b
        #this is how we keep track of the past two numbers to add together
        a,b = b,a+b
    return a  

#The recursive function seem simple and easy at first. It works great for
#single digit numbers. For me, the recursion solution tapped out at about 
#n = 35. This is becasue it has to calculate all the previous numbers more 
#than once and get all the way down to the base case every time. In an 
#iterative version using a for loop and swapping, it keeps track of the last 
#fibonacci number as you go through. The time complexity of a recursive 
#fibonacci solution is at least O(2^n) and probaly close to O(n!) due to using
#recursion twice, whereas an iterative fibonacci solution is just O(n).

#%% #6 showing moves plus ending state of stacks.
class Stack:
    def __init__(self, name):
        self.items = []
        self.name = name
        #added self.name to have a way to identify which stack is which

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() #built in function, returns item at end
                                #destructive, no longer on stack
    def peek(self):
        return self.items[len(self.items)-1]
                                #non-destructive, just see whats on top
    def size(self):
        return len(self.items)
    
    def __str__(self):
        string = ""
        for i in self.items:
            string = string + str(i)+ " "
        return(string)

#function to print out the moves required to move stack from pin A to pin B
#using the spare pin
def printMove(fr,to):
	print('move from ', fr.name, ' to ', to.name)
    

def stackTowers(n, a, b, spare):
    #error checking
    if n <1:
        raise ValueError("Tower height must be at least 1")
    #base case
    if n == 1:
        #print the move, and execute the move in the stack as well
        printMove(a,b)
        b.push(a.pop())
    #recursive moves to get to base case each time. Same code as example provided
    else:
        stackTowers(n-1, a, spare, b)
        stackTowers(1, a, b, spare)
        stackTowers(n-1, spare, b, a)
    #notify that task has been completed
    return ("Tower transfer complete: ")

#create the stacks that will be passed into the above function  
n = int(input("Tower of size: ")) #get tower size
#name the stacks so that moves can be printed
a = Stack('A')
b = Stack('B')
spare = Stack('Spare')

#iterate through range n to push numbers onto starting peg stack
for i in range(n, 0, -1):
    a.push(i)

#This is the code that actually calls the functions we made, as well as prints 
#the ending state of the three stacks.    
print(stackTowers(n, a, b, spare), a.name,a.items,spare.name,spare.items,b.name,b.items)

#%% #6 showing moves plus state of stacks throughout.
class Stack:
    def __init__(self, name):
        self.items = []
        self.name = name
        #added self.name to have a way to identify which stack is which

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() #built in function, returns item at end
                                #destructive, no longer on stack
    def peek(self):
        return self.items[len(self.items)-1]
                                #non-destructive, just see whats on top
    def size(self):
        return len(self.items)
    
    def __str__(self):
        string = ""
        for i in self.items:
            string = string + str(i)+ " "
        return(string)

#function to print out the moves required to move stack from pin A to pin B
#using the spare pin. Also prints the state of the stacks for visualization.
def printMove(fr,to,spare):
    #prints the state of the stack first, then the move to perform
    print(fr.name,fr.items,spare.name,spare.items,to.name,to.items, "\nmove from ", fr.name, " to ", to.name)
    

def stackTowers(n, a, b, spare):
    #error checking
    if n <1:
        raise ValueError("Tower height must be at least 1")
    #base case
    if n == 1:
        #print the move, and execute the move in the stack as well        
        printMove(a,b,spare)
        b.push(a.pop())
    #recursive moves to get to base case each time. Same code as example provided
    else:
        stackTowers(n-1, a, spare, b)
        stackTowers(1, a, b, spare)
        stackTowers(n-1, spare, b, a)
    #notify that task has been completed
    return ("Tower transfer complete: ")

#create the stacks that will be passed into the above function      
n = int(input("Tower of size: "))#get tower size
#name the stacks so that moves can be printed
a = Stack('A')
b = Stack('B')
spare = Stack('Spare')

#iterate through range n to push numbers onto starting peg stack
for i in range(n, 0, -1):
    a.push(i)

#This is the code that actually calls the functions we made, as well as prints 
#the ending state of the three stacks.
print(stackTowers(n, a, b, spare), "\n", a.name,a.items,spare.name,spare.items,b.name,b.items)
#%%