# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 13:25:57 2020

@author: Brooks Hanson
"""

#1
date = "3/2/2020"
def FullDate(date):
    mos = ['January','February','March','April','May','June','July','August','September','October','November','December']
    date = (date)
    split = date.split('/')
    month = int(split[0])
    day = split[1]
    year = split[2]
    print(str(mos[month-1]) + ' ' + str(day) + ', ' + str(year))
    
FullDate(date)


#2
ints = [1,2,3,4,5,6,7,8,9]
def squaredSumSquared(ints):
    listToStr = ' '.join([str(elem) for elem in ints]) 
    split = listToStr.split(' ')
    Sum = 0
    for i in split:
        sqr = int(i) * int(i)
        Sum = Sum + sqr
    root = Sum**(1/2)
    print(round(root,3))

squaredSumSquared(ints)


#3
phrase = "I like turtles"
def Acronym(phrase):
    phrase = phrase
    split = phrase.split(' ')
    ACN = ''
    for i in split:
        listToStr = ' '.join([str(j) for j in i]) 
        split2 = listToStr.split(' ')
        ACN = ACN + str(split2[0])
    print(ACN.upper())

Acronym(phrase)

#4
class PlayingCard:
    def __init__(self,rank,suit):
        try:
            if rank < 1 and rank > 13 and rank.lower() not in ["clubs","spades","diamonds","hearts"]:
                raise Exception
            else:
                self.rank = rank
                self.suit = suit
        except (Exception):
            print("Not valid card")
            
    def getSuit(self):
        suit = self.suit
        return(suit)
        
    def getValue(self):
        value = self.rank
        return(value)
    
c1 = ('3','clubs')   
card1 = PlayingCard(c1)     
            
        
    
    
    