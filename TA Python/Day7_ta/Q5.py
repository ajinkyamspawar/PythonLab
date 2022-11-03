# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 17:46:30 2022

@author: admin
"""

class temp:
    
    def __init__(self):
        pass
    def cel_to_far(self):
        a=float(input("Enter a cel"))
        f=(9/5)*a+32
        print(f)
    def far_to_cel(self):
        b=float(input('Enter the farn'))
        c=(b-32)*(5/9)
        print(c)
t=temp()
t.cel_to_far()
t.far_to_cel()       
