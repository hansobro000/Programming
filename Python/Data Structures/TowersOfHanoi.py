# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 13:16:04 2020

@author: Brooks Hanson
"""
#Piece can only move on top of other pieces larger than it
#move smallest piece every other move
#make only possible move not involving smalles piece in between small piece moves
#If number of pieces is odd, smallest piece order is start>target>spare>start
#If number of pieces is even, smallest piece order is start>spare>target>start
#repeat process until all pieces are on target pin
 


#%%
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 10:53:12 2019

@author: matth
"""
#%%

def printMove(fr,to):
	print('move from ', fr, ' to ', to)

def Towers(n,fr,to,spare):
    if n == 1:
        printMove(fr,to)
    else:
        Towers(n-1,fr, spare, to)
        Towers(1,fr, to, spare)
        Towers(n-1,spare, to, fr)
    
#%%

Towers(0,'A','B','Spare')  
Towers(4,'A','B','Spare')  
#%%
def printMove(fr,to):
	print('move from ', fr, ' to ', to)

def T2(height,fromPole,toPole,withPole):
    if height >= 1:
        T2(height-1,fromPole,withPole,toPole)
        printMove(fromPole,toPole)
        T2(height-1,withPole,toPole,fromPole)
#%%
T2(3,'A','B','Spare')  
T2(4,'A','B','Spare')  
