# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 13:31:20 2020

@author: Brooks Hanson
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 19:34:19 2019

@author: matth
"""
#%%
#reset environment
from IPython import get_ipython
get_ipython().magic('reset -sf')

from time import *

#%%
#Notes:

#log(n) is the time it takes to halve a sorted list until you get to 
#the end

#n(log(n)) log linear is the sorting question. is it faster to sort first
# and then find

#for loop inside a for loop when both are linear, is n^2. add
# a third for loop and you get cubic, then to the 4th 5th ect.

#focus on most dominant in function
#%%
# sum 1


def sumOfN(n):

    begin = time()
    
    s = 0
    for i in range(n+1):
        s = s + i
    
    end = time()
    
    return(s, end - begin)
    
#%%

print('sum first 10000')
for i in range(5):
    print('Sum is %d required %10.7f seconds'%sumOfN(10000))

print('sum first 10000000')
for i in range(5):
    print('Sum is %d required %10.7f seconds'%sumOfN(1000000))

#%%

#sum 2

def sumOfN2(n):
    begin = time()
    s = (n*(n+1))/2 #summation of any integer
    end = time()
    return(s,end-begin)

#%%

print('sum first 10000')
for i in range(5):
    print('Sum is %d required %10.7f seconds'%sumOfN2(10000))

print('sum first 10000000')
for i in range(5):
    print('Sum is %d required %10.7f seconds'%sumOfN2(1000000))
   
#back to slides       
    
#%%
# anagram solver 1

def anagramSolver1(s1,s2):
    
    if len(s1) != len(s2):
        return(False)
        
    s1.upper()  # don't be case sensitive
    s2.upper()
    
    l = list(s2)    
        
    p1 = 0
    ok = True
    
    while p1 < len(s1) and ok:
        p2 = 0
        found = False
        while p2 < len(l) and not found:
            if s1[p1] == l[p2]:
                found = True
            else:
                p2 += 1
        if found:
            l[p2] = None
        else:
            ok = False
            
        p1 += 1
    
    return(ok)

#n2, longest
    
#%%

print(anagramSolver1('tear','rate'))    

print(anagramSolver1('tear','tone'))

#%%

#Anagram solver 2

def anagramSolver2(s1,s2):
    
    if len(s1) != len(s2):
        return(False)
    
    s1.upper()  # don't be case sensitive
    s2.upper()
    
    l1 = list(s1)
    l2 = list(s2)
    
    l1.sort()     #this is an n(log(n)) algorithm
    l2.sort()

    p = 0
    ok = True
    
    while p < len(s1) and ok:
        if l1[p] == l2[p]:
            p = p + 1
        else:
            ok = False
            
    return(ok)

#n+nlog(n), second longest
    
#%%    


print(anagramSolver2('tear','rate'))    

print(anagramSolver2('tear','tone'))


#%%

#Anagram solver 3

def anagramSolver3(s1,s2):
    
    if len(s1) != len(s2):
        return(False)
        
    s1.upper() # don't be case sensitive
    s2.upper()    
        
    c1 = [0]*26     # create a list of with 26 cells equal to zero
    c2 = [0]*26

# ord() returns the unicode value for the character
# A = 65, B = 66, C = 67... Z = 90

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('A')
        c1[pos] = c1[pos] + 1    # increment the count we have for this letter
    
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('A')
        c2[pos] = c2[pos] + 1
        
    j = 0
    ok = True
    while j < 26 and ok:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            ok = False
            
    return(ok)

#n, shortest

#%%
print(anagramSolver2('tear','rate'))    

print(anagramSolver2('tear','tone'))