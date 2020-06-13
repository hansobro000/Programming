# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 13:25:24 2020

@author: Brooks Hanson
"""

#%%
x = 4
2+3*4

2**10       #exponential
pow(2,10)   #expenential

7/3     #returns float
7//3    #integer division. Truncates, does not round

7%3     #Hashing, gives remainder

#Variables
x = 5
y = 6
z = x + y

#Print
print (z)
print ("Addition " + str(x+y))
print ("Addition $" + str(x+y))
print("Addition",x+y)

# Float
f = 3.54
g = 2.46
print(f)
print(f+g)
print(f*g)

# Relational/boolean
# case sensative

True == False   #comparison operator
True or False   #if anything on either side of the or is true, then true
1 == 3 or 4 == 4

2 == 3 and 4 == 4   #for and, both sides need to be true

True or False and True      #true
True or (False and True)    #true
(True or False) and True    #True
True and not False          #True
False and not True          #False
False or not True           #False
True or not False           #True

x = 2

2 <= x < 8  #True

==  #equal
<   #less than
<=  #less than or equal to
>   #greater than
>=  #greater or equal to
!=  #not equal to


# String: a basic type, but also a collection
# Objects have two things: Attributes and Methods


print("Hello World")
strng = "Hello World"
print(strng)

print(strng.upper())
print(strng.find('o')) # First occurance. Python is Zero based

print(len(strng))

print(strng[1])
print(strng[:2])
print(strng[:-2])

print(strng[1:12:2])


# string Formatting

pName = 'Brooks'
pFeet = 6
pInches

print("Brooks", "Hanson")
print("Brooks","Hanson",sep=', ') #seperator

print("Name is %s." % (pName))

#%% InClassPractice

f = "Brooks"
l = "Hanson"
age = "20"

print(f + l + age)
print(f, l, age)

print(f.upper())

print(l[:2])

print(f[0].upper() + l[0].upper())

print(5%3)



#%% Colelction Types

mylist = [1,2,3,5,8,13,21,34]

#other operations
print( 21 in mylist)
print(mylist.index(21))
print(mylist.count(21))

mylist.append(21)
print(mylist)

print(sorted(mylist)) #prints sorted version of list
mylist.sort() #modifies list to be sorted
mylist.remove(21)
mylist.reverse()

#init a list with 10 strings

mystrlist = ["Hello"]
type(mystrlist)

mystrlist = mystrlist * 10
print(mystrlist)

mystrlist[0] = "World"  #mutability
print(mystrlist)


# copy vs deep copy

list1 = [1,2,3,4]
list2 = list1

list1[0] = "What's going on here"
print(list2)
# Above makes a copy that points to the address of the first one

import copy

list3 = ['a', 'b', 'c', 'd']
list4 = copy.copy(list3)
list3[0] = 3.145
print(list3)
print(list4)
#above makes a deep copy that duplicates the contents of the first

#%% Range work

print(range(10))
print(list(range(10)))
print(list(range(5,10)))
print(list(range(0,10)))

#%% Tuples - Kind of like lists, but immutable

mytuple = (1,2,3,5,7,9,11)
print(mytuple)
print(len(mytuple))
print(mytuple[1])
type(mytuple)

print(mytuple[1]) #idex the same using brakets, not parens
# dont care about datatype

tuple2 = ("string",1,2,False,["list","of", "strings"])
print(tuple2)

print(tuple2[4])
print(tuple2[4][1])

tuple2[4][1] = "does this work?"
print(tuple2[4])
# a tuple is immutable, a list inside the tuple isnt

#%% sets - GET RID OF DUPLICATES
# cant store duplicates. If you have duplicates and throw it into a set,
# it will strip the duplicates

imgur = {"Cats","Dogs","First world problems"}
print(len(imgur))
print(imgur[1]) #cant do this. sets are unordered. object

reddit = {'Cats','dogs','nfl_gamethread'}

print(imgur | reddit) # bitwise operator for or
print(imgur & reddit) # bitwise operator for and

#%% dictionaries
# key - value pair
# a way to acces information by the key rather than the
# number place it occupies

# use numbers or strings so that it is hashable


#%%
turning list into set using type casting

l1 = [1,2,3,4]
s1 = set(l1)
type(s1)

l2 = [1,1,1,1,1,1,1,1,2,3,4,5]
print(l2)

s2 = set(l2)
print(s2)


l2 = s2
print(l2)

#%% InClassPractice

list5 = ['Alpha','Beta','Gamma','Delta','Epsilon','Zeta','Eta','Theta','Iota']
print(list5)

list5.sort()
print(list5)

print(list5[2])
print(list5[8])
print(list5[-1])
print(list5[-2])
print(list5[-0])
