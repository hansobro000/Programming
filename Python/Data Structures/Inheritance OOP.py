# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 13:42:12 2020

@author: Brooks Hanson
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 08:42:41 2018

@author: matth
"""


class employee(): # base class
    def __init__(self,fname,lname,r): #Constructor method
        self.firstName = fname
        self.lastName = lname
        self.email = lname+fname[0]+"@acme.com"
        self.hourlyRate = r/2080
        
    def __str__(self): #allows us ot use the print function
        return(self.lastName + ', ' + self.firstName)
        
    def __add__(self,str2): # overwrites the plus opperator
        return(str(self) + str2)    # str(self) calls the above method, __str__ 
                                    # and makes the last name, firstname a string
                                    # then it adds the second name to it
        
class hourlyEmployee(employee): # No constructor becuase it inherits it
                                # from the employee class
     
    pay = 0
    def calcPay(self,h=40):
        if h > 40:
            pay = self.hourlyRate * 40 + self.hourlyRate * 1.5 * (h-40)
        else:
            pay = self.hourlyRate * h
        return(round(pay,2))
        
        
class salaryEmployee(employee):
    
    def calcPay(self,r):  #hours ignored for salaried employees
        return(round(self.hourlyRate * 40,2))
    
#%%

staffMember = hourlyEmployee("Matt", "Heinrich",30000)

managementMember = salaryEmployee("Lisa","Heinrich",50000)

print(staffMember + '  email: ' + staffMember.email)
print(managementMember + '  email: ' + managementMember.email)


print(" 35 hours worked")
print(staffMember + ' Current Pay: ' + str(staffMember.calcPay(35)))
print(managementMember + ' Current Pay: ' + str(managementMember.calcPay(35)))

print(" 40 hours worked")
print(staffMember + ' Current Pay: ' + str(staffMember.calcPay(40)))
print(managementMember + ' Current Pay: ' + str(managementMember.calcPay(40)))

print(" 45 hours worked.")
print(staffMember + ' Current Pay: ' + str(staffMember.calcPay(45)))
print(managementMember + ' Current Pay: ' + str(managementMember.calcPay(45)))