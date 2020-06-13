# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 13:32:12 2020

@author: Brooks Hanson
"""

#%%

#reset environment
from IPython import get_ipython
get_ipython().magic('reset -sf')

from StackClass import *
#%%

def palindrome(wordstring):
    
    s = Stack()
    
    for i in wordstring:
        s.push()
            
    reverseWord = ''
    
    while not s.isEmpty():
        reverseWord = reverseWord + s.pop()
    
    if wordstring == reverseWord:
        return("You have a palindrome")
    else:
        return("You do not have a palindrome")
    

string = "race car"
print(palindrome(string))
#%%

def flipsentance(sentence):

    s = Stack()
    
    data = sentence.split() #split string into a list
    
    for temp in data:
        s.push(temp)
        
    reverseSentence = ''
    
    while not s.isEmpty():
        reverseSentence = reverseSentence + ' ' + s.pop()
    
    return(reverseSentence)

stringtest = "Hello my name is Brooks"
print(flipsentance(stringtest))
#%%
# create a sort routine that will sort a stack using a temporary stack
def stacksort(numberlist):
    
    s = Stack()
    
    for i in numberlist:
        s.push()
    
    temp = Stack()
    
    while temp.isEmpty():
        temp = s.pop()
    
        while not temp.isEmpty() and temp.peek() > temp:
#%%
