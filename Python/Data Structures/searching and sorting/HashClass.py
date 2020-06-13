# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 14:59:05 2020

@author: Brooks Hanson
"""

# Hash table class
# uses simple remainder for hash value
# uses open addressing
# linear probing
# will overwrite if we run out of empty slots.


class HashTable:
    def __init__(self,size):
        self.slots = [None] * size
        self.data = [None] * size
        
    def search(self,item):
      startslot = self.hashfunction(item,len(self.slots))

      data = None
      stop = False
      found = False
      position = startslot
      while self.slots[position] != None and  \
                           not found and not stop:
         if self.slots[position] == item:
           found = True
           data = self.data[position]
         else:
           position=self.rehash(position,len(self.slots))
           if position == startslot:
               stop = True
      return data

    def __getitem__(self,item):
        return self.search(item)

    def __setitem__(self,item,data):
        self.store(item,data)

    def store(self,item,data):
      hashvalue = self.hashfunction(item,len(self.slots))

      if self.slots[hashvalue] == None:
        self.slots[hashvalue] = item
        self.data[hashvalue] = data
      else:
        nextslot = self.rehash(hashvalue,len(self.slots))
        while self.slots[nextslot] != None:
          nextslot = self.rehash(nextslot,len(self.slots))

        self.slots[nextslot]=item
        self.data[nextslot]=data

    def hashfunction(self,item,size):
             return item%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size