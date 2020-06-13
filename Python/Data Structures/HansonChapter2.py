# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 13:51:06 2020

@author: Brooks Hanson
"""

#%%
#Programming Exercise 4


#using selection sort algorithm from 'Sorting Algorithms in Python' by 
#Marcus Sanatan on stackabuse.com

def kthSmallest(nums,k):
    nums = set(nums)    #turn list into a set to remove duplicates
    nums = list(nums)   #turn list back into a list so that it is 
                        #subscriptable
    #sort the list
    for i in range(len(nums)):
        low = i         #assign first number in list as lowest value to start
        for j in range(i +1, len(nums)):    #iterate over the unsorted numbers
            if nums[j] < nums[low]:
                low = j
        nums[i], nums[low] = nums[low], nums[i] #Swap the lowest number with 
                                                #the first number
    #return the kth smallest number in the now sorted list
    print("The kth smallest number in your list is: ", nums[k-1])
    #Since a list is zero based, k-1 makes the index number match the 
    #desired K value.

#The time complexity of this algorithm is O(n^2) because it takes a loop 
#inside of a loop to sort the random list of numbers.

#%%
#Example test
randomList = [3,5,8,5,3,1,9,0]
kthSmallest(randomList,4)
