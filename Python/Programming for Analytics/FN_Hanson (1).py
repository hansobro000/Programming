#%%

# Question 1


def main():
    print("This program returns the brand of a valid credit card number.")
    
    card = str(input("\nEnter your credit card number: "))
    
    length = len(card)
    brand = int(card[0])

    if length == 16 and brand == 4:
        print("Your card is a Visa")
    elif length == 16 and brand == 5:
        print("Your card is a MasterCard")
    elif length == 16 and brand == 6:
        print("Your card is a Discovery") 
    else:
        print("Unknown Card")
    
main()

# good

#%%

# Question 2

def main():
    
    MyGuess = 5
    
    g = int(input("Guess my favorite number. "))
    while g != MyGuess:
        if g < MyGuess:
            print("Guess Higher")
        else:
            print("Guess Lower")
        g = int(input("Guess my favorite number. "))
        
main()

# good
#%%

# Question 3

def main():
    
    print("This prgram calculates the sale price of an item.")
    
    regular = float(input("Regular price: "))
    sale = int(input("Percent off: "))
    percent = sale / 100
    
    newPrice = regular * (1-percent)
    
    print("Sale price: ${:,.2f}".format(newPrice))
    
main()

# good
#%%

# Question 4

class CashRegister:
    
    def __init__(self):
        self.total
    
    def startTransaction(self):
        self.total = 0.00
    
    def addItem(self, amount):
        self.total = self.total + amount
        
    def total(self):
        return self.total

def main():
    
    register1 = CashRegister()
    
    print("Please enter the amount of each item. Hit enter again to quit.")
    
    register1.startTransaction()
    amount = float(input("Price of item: "))
    while amount != '':
        register1.addItem(amount)
        amount = float(input("Price of item: "))
    print("The total amount due is: $", register1.total())
    
main()

'''
The problem you run into here is having an attribute total (self.total) and a method total()
One of them is going to be hidden outside of the actual class.  You're correct
that you have the general structure of the code and the logic correct. Avoid
duplicating names.
You also have an issue with just hitting enter to exit, that causes your input statement
to crash.  Python float(),int() etc doesn't like empty entries. 
'''

#%%

# Question 5
        

def main():
    
    print("This program simulates an automatic change dispenser.")
    
    due = int(input("How much change is due? "))
    
    if due >= 0 and due <= 99:
        print("\nChange due:")
        
        quarters = due // 25
        due %= 25
        if quarters > 0:
            print(quarters, "Quarters")
        
        dimes = due // 10
        due %= 10
        if dimes > 0:
            print(dimes, "Dimes")
        
        nickles = due // 5
        due %= 5
        if nickles > 0:
            print(nickles, "Nickles")
        
        pennies = due // 1
        if pennies > 0:
            print(pennies, "Pennies")
    else:
        print("Please enter a number from 0 to 99.")
    
main()

# good

#%%

