# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 14:38:04 2020

@author: matth
"""

# 1.	Create a function that returns a date in the format of 
# March 2, 2020 when passed a date in the format 3/2/2020.  
# No need to perform error checking on a valid date.

#%%
def prettyDate(dateIn):
    mdy = dateIn.split('/')  # split the inbound parameter by the / in the date
    mnth = ['January','February','March','April','May','June','July','August','September','October','November','December']

    return(mnth[int(mdy[0])- 1] + ' ' + str(int(mdy[1])) + ', ' + str(mdy[2]))

# subscript mnth list with month value - 1, 
# int on the day value gets rid of potential leading zeroes



#%%

# test a couple. 
d = '03/02/2020'
print(prettyDate(d))
d1 = '12/31/2020'
print(prettyDate(d1))    

#%%

'''
2.	Create a function that accepts a list of integers (Error checking not required). 
Return a list that is the square root of the sum of all of the integers squared. 
Print the returned value rounded to three digits to the right of the decimal point.
e.g. [1,2,3] would return the square root of 14. You would print 3.742
'''

def foo(inList):
    tempval = 0
    retList = []
    for x in inList:
        tempval = tempval + x**2
    retList.append(tempval**.5)
    return(retList)

# kind of stupid to return a list for this function, but that's what the moron
# asked for in the question so that's what he's going to get back. 
# raised final value to the 1/2 power to get the square root. Could also use
# the sqrt function in the math library.
    
myList = [1,2,3]
myFloat = foo(myList)

print('%0.3f' % myFloat[0])
# lots of different ways to format but this is one example
# 0.3f says always use 3 decimal points and as many digits to the left as necessary

myList2 = [1,1,1,1]
myFloat2 = foo(myList2)
print('%0.3f' % myFloat2[0])

#%%

'''
3.	Create a function that returns an acronym of a passed string. Response should be in all caps.
e.g. “random access memory” should return RAM
      “People can’t memorize computer industry acronyms” should return PCMCIA

'''


def acronym(s):
    temps = s.upper().split() # yes you can combine this kind of stuff
    retval = ""
    for x in temps:
        retval = retval + x[0]
    return(retval)

    
print(acronym('Hello World'))
print(acronym('Helzberg School of Management'))

#%%

'''
4.	Create a playing card class.  

Attributes should include rank/number of a card and a suit. There are 4 suits (Clubs, Spades, Diamonds, Hearts) There are 13 ranks/number per suit (1-13, ace=1, king = 13).

Methods should include:
a.	Constructor. Error checking should be performed here. For example, I can’t have a rank that is < 1 or > 13, suits have to be clubs, spades, diamonds, hearts.
b.	getRank – return the rank of the card. For Jack, Queen, King, Ace that text should be returned. For all others the number is fine.
c.	getSuit- return (Club, Diamond, etc.)
d.	getValue – return numerical value of the card (1 – 13, ace = 1, king = 13)
Calling print(card) should result in something that looks like this: “Ace of Spades”, “10 of Clubs”, “Jack of Diamonds”, etc.

'''

class card:
    def __init__(self,r,s):
        err = False
        if isinstance(r,int) != True:
            err = True
        elif r < 1 or r > 12:
            err = True
        
        if isinstance(s,str) != True:
            err = True
        elif s.upper() not in ('CLUB','SPADE','DIAMOND','HEART'):
            err = True
            
        if err:
            raise ValueError("invalid parameter passed to card constructor. Rank should be integer (1-13)\nSuit should be Club, Spade, Diamond, or Heart")

        self.r = r
        self.s = s.lower().title() # make sure it only has the first letter capped.

         
    def getRank(self):
        retval = ""
        faceCards = ['Jack','Queen','King'] # handle the face cards
        if self.r > 9:
            retval = faceCards[self.r-10]
        elif self.r == 1:
            retval = 'Ace'          # handle the ace
        else:
            retval = str(self.r)
        return(retval)
    
    def getSuit(self):
        return(self.s)
    
    def __str__(self):
        retval = self.getRank() + ' of ' + self.getSuit() + 's'
        return(retval)
        
#%%

# run some tests
        
c1 = card(8,'spade')        
print(c1.getRank())
print(c1.getSuit())     

print(c1)   


c2 = card(1,'heart')
print(c2)

c3 =card(12,'club')
print(c3)

c4 = card(8,'potato')
c5 = card(75,'Heart')
c6 = card(8,9)
c7 = card('hello','Heart')

#%%
'''
5.	Create a temperature conversion chart for Fahrenheit/Celsius.
Fahrenheit = 32 + 9/5*Celsius
Print the chart out in a format like the below. Fahrenheit temp should range from 0 – 100 	in 5-degree increments, Celsius temperature should correspond to that Fahrenheit temp.
Fahrenheit Temperature	Celsius Temperature
0	-17.78
5	-15
.   .
.   .
.   .
100	37.78

'''

def fcTable():
    retVal = "Fahrenheit Temperature\tCelsius Temperature\n" #\t is tab character
    for x in range(0,105,5):
        ftemp = x
        ctemp = round((ftemp - 32) * 5 / 9,2) # round not specified but prettier
        retVal = retVal + '{0:15.2f}'.format(ftemp) + '{0:21.2f}'.format(ctemp) + "\n"
    return(retVal)        

print(fcTable())




#%%        
            
