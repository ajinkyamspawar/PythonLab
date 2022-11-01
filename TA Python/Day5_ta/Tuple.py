# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 04:10:17 2022

@author: admin
"""

#Ass1------
t1=(1,2,3,4)
#L3=[(i**=j) for i in L1 for j in L2 range(0,4)]--Don't do by this way
L3=[(i,i**2) for i in t1]
print(L3)

#Ass2-----
t=("a","e","i","o","u","A","E","I","O","U")
v=str(t)
print(v)
type(v)
type(t)


#Ass3-----
num=(1,2,3,4)
num1=(5,6,8,7)
print(num+num1) #3.2
print(num) #3.1
print(num1) #3.1
#type(num)
#type(num1)
combo2=sorted(num+num1)

print(combo2) #3.3
a=combo2 [2] #3.4
print(a)    #3.4

b=combo2[-3:] #3.5
print(b)    #3.5

c=combo2[-1::-1]
print(c)
print(len(combo2)) #3.6

#Ass4--
t1=(1,"Hello","a",2,"b")
a=t1[1][4]
print(a)
b=t1[3]
print(b)

#Ass5---
tuple=(1,2,5,6,3,8,5,2,1,4,6)
no=int(input("Enter a number"))
print(tuple.count(no))

#Ass6-----

tuple=(1,2,3,4,5,"r")
no=input("Enter any velement to check extst")
if no.isdigit():
    no=int(no)
    
else:
    no = no
    
print(no in tuple)















    



