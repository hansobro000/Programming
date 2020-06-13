# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 13:44:34 2020

@author: Brooks Hanson
"""
#%% Implement a stack using a linked list

from NodeClass import *

class LStack:
    def __init__(self): #constructor
        self.head = None
        
    def isEmpty(self):  #None is the default head of a linked list, so if
        return(self.head == None)   #the head equals None, it must be empty

    def push(self,data):        #pass whatever data we wish
        temp = Node(data)       #create a node with passed data
        temp.setNext(self.head) #point new node at previous head
        self.head = temp        #set new node as the head
        
    def pop(self):
        if self.head == None:   #can't pop something off if stack is empty
            return("Stack is Empty") #if empty, say so instead of crashing
        else:
            current = self.head #capture current head for future use
            self.head = current.getNext() #new head is now current next
            return(current.data) #show the data from the head before we set 
                                 #it to the next node in stack.
        
    def peek(self):
        if self.head == None:
            return("Stack is Empty")    #make sure stack isn't empty
        else:
            return self.head.data       #return the data from head node
    
    def length(self):
        current = self.head
        count = 0
        #general accumulator. loop through stack adding 1 to the count for each
        #node encountered until we reach none, the end of a linked list.
        while current != None:
            count = count +1
            current = current.getNext()
        return(count)
    
    def __str__(self):
        current = self.head    
        retstr = ""
        #Override __str__ method so we can use built in print.
        #Same as length process, except concatenating the data from each node
        #into a string, moving to the next line after each concat
        while current != None:
            retstr = retstr + str(current.data) + "\n"
            current = current.getNext()
        return(retstr)

#%% Implement a queue using a linked list

from NodeClass import *

class LQueue:
    def __init__(self): #Constructor
        self.head = None
        
    def isEmpty(self):  #None is the default head of a linked list, so if
        return(self.head == None)   #the head equals None, it must be empty
    
    def enqueue(self,data):     #pass whatever data we wish
        temp = Node(data)       #create a node with passed data
        temp.setNext(self.head) #point new node at previous head
        self.head = temp        #set new node as the head
        
    def dequeue(self):
        current = self.head #capture current head
        previous = None     #create way to track previous node
        stop = False        #create way to stop at end of LL
        
        if current == None: #Make sure queue isnt empty
            return("Queue is Empty")
        
        #loop to end of queue, stopping at last node before None
        #This is the first node created
        while not stop and current != None:
            if current.getNext() == None:
                stop = True
            #if there is more than one node in the queue, variable previous
            #needs to be set to the current head; loop on to the next node
            else:
                previous = current
                current = current.getNext()
        #Once complete, the last node in the queue is stored in the
        #variable current, and the node before it is stored in previous
        
        #if only one node in queue, set the head to None, effectively dequeueing
        #the node
        if previous == None:
            self.head = current.getNext()
        #if queue longer than one node, set the previous node to point to the 
        #current node's next. This effectively dequeues the last node because 
        #it has been eliminated from the chain of pointers
        else:
            previous.setNext(current.getNext())
        
        #return data that got dequeued
        return(current.data)
    
    def length(self):
        current = self.head
        count = 0
        #general accumulator. loop through queue adding 1 to the count for each
        #node encountered until we reach None, the end of a linked list.
        while current != None:
            count = count +1
            current = current.getNext()
        return(count)
    
    def __str__(self):
        current = self.head    
        retstr = ""
        #Override __str__ method so we can use built in print.
        #Same as length process, except concatenating the data from each node
        #into a string, moving to the next line after each concat
        while current != None:
            retstr = retstr + str(current.data) + "\n"
            current = current.getNext()
        return(retstr)

#%% Implement a deque using a linked list

from NodeClass import *

class LDeque:
    def __init__(self): #Constructor
        self.head = None
        
    def isEmpty(self):  #None is the default head of a linked list, so if
        return(self.head == None)   #the head equals None, it must be empty
    
    def addFront(self,data):    #pass whatever data we wish
        temp = Node(data)       #create a node with passed data
        temp.setNext(self.head) #point new node at previous head
        self.head = temp        #set new node as the head
        
    def addRear(self,data): #pass whatever data we wish
        current = self.head #keep track of current head
        stop = False        #create way to stop at end of LL
        
        if current == None:
            #If deque is empty, same as addFront
            temp = Node(data)
            temp.setNext(self.head)
            self.head = temp
        
        while not stop and current != None:
            #loop through deque, stopping at the last node
            if current.getNext() == None:
                stop = True
            else:
                current = current.getNext()
        #the last node is now stored in the variable Current
        
        #create a new node with passed data, and set the current node to point
        #to this new node
        else:
            temp = Node(data)
            current.setNext(temp)
        
    def removeFront(self):
        #check that deque isnt empty
        if self.head == None:
            return("Deque is Empty")
        #pop off first node in the deque. Make next node the new head
        else:
            current = self.head
            self.head = current.getNext()
            return(current.data)
    
    def removeRear(self):
        current = self.head #capture current head
        previous = None     #create way to track previous node
        stop = False        #create way to stop at end of LL
        
        if current == None: #Make sure deque isnt empty
            return("Deque is Empty")
        
        #loop to end of deque, stopping at last node before None
        #This is the first node created
        while not stop and current != None:
            if current.getNext() == None:
                stop = True
            #if there is more than one node in the deque, variable previous
            #needs to be set to the current head; loop on to the next node
            else:
                previous = current
                current = current.getNext()
        #Once complete, the last node in the deque is stored in the
        #variable current, and the node before it is stored in previous
        
        #if only one node in deque, set the head to None, effectively popping
        #off the node        
        if previous == None:
            self.head = current.getNext()
        #if deque longer than one node, set the previous node to point to the 
        #current node's next. This effectively popps off the last node because 
        #it has been eliminated from the chain of pointers
        else:
            previous.setNext(current.getNext())
        
        #return data that got popped off
        return(current.data)
    
    def size(self):
        current = self.head
        count = 0
        #general accumulator. loop through deque adding 1 to the count for each
        #node encountered until we reach None, the end of a linked list.
        while current != None:
            count = count +1
            current = current.getNext()
        return(count)
    
    def __str__(self):
        current = self.head    
        retstr = ""
        #Override __str__ method so we can use built in print.
        #Same as length process, except concatenating the data from each node
        #into a string, moving to the next line after each concat
        while current != None:
            retstr = retstr + str(current.data) + "\n"
            current = current.getNext()
        return(retstr)

