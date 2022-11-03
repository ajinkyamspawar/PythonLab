# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 14:37:18 2022

@author: admin
"""
#Before declaring global
sum1=-5
def add(a,b):
    sum1=a+b
    return sum1
print(add(3,6))
print(sum1)

#After declaring global

sum1=-5
def add(a,b):
    global sum1
    sum1=a+b
    return sum1
print(sum1)
print(add(4,4))
print(sum1)
print(add(5,5))
print(sum1)



    