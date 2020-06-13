'''
CS 3000 Final - Coding
'''

#%%
'''
Coding Exercise #1 (15 points)

Using the random library, create a random 50 element list of integers
ranging from 1 - 100.

Create a function that will accept one list type parameter.
In the function split the passed list into two separate lists, 
one that has the even numbers and one that has the odd numbers. 
Return both lists in sorted order from the function.

Provide code to create the original list, call the function passing the 
original list, and print the returned lists. The function you create should
not print anything. You do not need to perform error checking.

list Examples:

Original random list = [94,46,1,64,31,67,100,7,89,47,83,49,81,50,19,76,44,59,35,69,12,52,10,17,18,15,9,36,28,74,20,3,60,85,98,42,30,33,78,4,22,80,41,51,93,45,2,66,96,86]
new lists
[2,4,10,12,18,20,22,28,30,36,42,44,46,50,52,60,64,66,74,76,78,80,86,94,96,98,100]
[1,3,7,9,15,17,19,31,33,35,41,45,47,49,51,59,67,69,81,83,85,89,93]


'''
#import random library
import random

#easy bubble sort function to sort random list
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1]=alist[i+1],alist[i]

#create random list of 500 integers
randomList = []
for i in range(50):
    n = random.randint(1,100)
    randomList.append(n)

#function to split random list
def listSplitter(ran):
    #sort random list
    bubbleSort(ran)
    
    #create empty new lists
    even = []
    odd = []
    
    #append the even and odd numbers in the random list to cooresponding lists
    for i in ran:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    #return the new lists with a linespace
    return('{0}\n{1}'.format(even, odd))

#print new the random list split into sorted even and odd lists
print(listSplitter(randomList))



#%%


'''
Coding Exercise #2 (25 points)

Create a function that requires a user to create a password.

The password should be entered twice and the values entered must match.
Matching should be case sensitive.

Passwords must be a minimum length of 8 characters.
Passwords can only contain alpha or numeric characters, no special characters 
e.g. space, @, #, &, etc.
Passwords must contain at least one upper case letter.
Passwords must contain at least one lower case letter.
Passwords must contain at least one number.

The function should repeat until a valid password has been created. If the
entered password does not conform to the above rules, an appropriate message
should be given to the user indicating what failed. 

The created password should be returned by the function when valid. 


'''
#referencing password vailidation from https://www.geeksforgeeks.org/password-validation-in-python/

# Password validation in Python 
# using naive method 
  
# Function to validate the password 


def password_check(passwd): 
      
    val = True
    SpecialSym =['$', '@', '#', '%', ' ', '&', '!', '%', '*']
      
    if len(passwd) < 8: 
        print('length should be at least 8') 
        val = False
          
    if not any(char.isdigit() for char in passwd): 
        print('Password should have at least one numeral') 
        val = False
          
    if not any(char.isupper() for char in passwd): 
        print('Password should have at least one uppercase letter') 
        val = False
          
    if not any(char.islower() for char in passwd): 
        print('Password should have at least one lowercase letter') 
        val = False
    
    if any(char in SpecialSym for char in passwd): 
        print('Password should not contain any special symbols') 
        val = False
        
    if val: 
        return val 


  
# Main method 
def main(): 
    passwd = input("Enter password: ")
    passwd2 = input("Enter password again: ")
    

    if passwd.upper() != passwd2.upper():
        raise ValueError("Passwords don't match")
    
    else:
      
        if (password_check(passwd)): 
            print("Password is valid", passwd) 

        else: 
            print("Invalid Password !!") 

          
# Driver Code         
if __name__ == '__main__': 
    main() 

#%%
'''
Coding Exercise #3 (25 points)


Write a recursive function that calculates the sum of the squares of variation
between a list and a constant value.

example.
List = [10,2,9,15,18,12]
Constant = 7

Below, ^2 means to square (raise to the power of 2)
e.g. 10 - 7 = 3. 3^2 = 9

(10 - 7)^2 = 9
(2 - 7)^2 = 25
(9 - 7)^2 = 4
(15 - 7)^2 = 64
(18 - 7)^2 = 121
(12 - 7)^2 = 25

9 + 25 + 4 + 64 + 121 + 25 = 248

Function should accept 2 parameters, the list e.g [10,2,9,15,18,12] and the constant e.g. 7
Function should return the sum of squared variation e.g. 248

Include a test scenario that demonstrates the code
Error checking is not required


'''

def ssvR(lst,constant):
    if (lst[i] == (len(lst)-1)):
        return 0
    else:
        return (ssvR(lst[i]-constant)+ n*n)        