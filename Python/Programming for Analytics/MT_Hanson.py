# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 22:08:47 2019

@author: brook
"""
#%%

# 1 - "Even integers"

# This program prints the even integers from 2 to 20.

def main():
    print("\nThe even integers from 2 to 20 are:")
    for int in range(2,21):
        if int % 2 == 0:
            print(int)
        
main()

# good

#%%

# 2 - "Rover to earth transmit time"

# This program calculates the amount of time it takes a signal from the Mars
# rover to transmit to NASA on earth; traveling at the speed of light; at
# Mars' closest disatnce to earth.

def main():
    print("\nThe closest that Mars gets to Earth in its orbit is 34,000,000"
          " miles away.")
    dist = 34000000
    time = dist / 186000 
    minutes = time / 60
    print("\nIf the Mars rover transmits an image at this distance at the" 
          " speed of light; the signal will take", round(minutes,2), "minutes"
          " to reach NASA.")
    
main()

# good

#%%

# 3 - “Wheat and chessboard problem”

# This program doubles the dumber of 'wheat' on subsequent tiles of a chess
# board until it reaches the 64th and final tile; printing the 64th tile's total.

def main():
    wheat = 1
    count = 1
    for i in range(64):
        wheat = wheat * 2
        count = count + 1
    print("\nOn the last square of the chessboard, there will be"
          " {:,}".format(wheat), "wheat.")
    
main()

#good

#%%

# 4 - "Letter Counter"
# This program counts the number of times a specified character occurs in a 
# given string.

def main():
    string = str(input("Enter any sentence or phrase: "))
    letter = str(input("\nWhat character would you like to find? "))
    print("\nThere are", string.count(letter), letter+"'s in your string")
    
main()

# good

#%%

# 5 - "Passing a bill"

# This program returns 'True' if a bill has passed given what house it is in 
# and what the number of 'yea' votes are, or 'False' if it did not pass. 
# There is input validation for body of congress and number of "yea's"

def main():
    
    print("\nThis program returns 'True' if the bill has passed and 'False'"
          " if it did not pass")
    congress = input("Is the bill currently in the house or in the senate? ")
    while congress[0] != "h" and congress[0] != "H" and congress[0] != "s"\
        and congress[0] != "S":
        print("\n'"+str(congress)+"' is not the House nor the Senate..." 
              " please enter a valid body of congress.")
        congress = input("Is the bill currently in the house or in the senate? ")
    result = int(input("How many 'yea' votes were given? "))
    while ((congress[0] == "h" or congress[0] == "H") and (result <= 0 or result >= 435))\
        or ((congress[0] == "s" or congress[0] == "S") and (result <= 0 or result >= 100)):
        print("\nThere are 435 seats in the House and 100 seats in the Senate..."
              " please enter a valid vote count.")
        result = int(input("How many 'yea' votes were given? "))
    if ((congress[0] == "h" or congress[0] == "H") and result >= 218) or \
        ((congress[0] == "s" or congress[0] == "S") and result > 50):
        print("\nTrue")
    else:
        print("\nFalse")
main()        

# good - nice error checking.

#%%
  