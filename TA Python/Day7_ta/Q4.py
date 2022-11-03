# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 17:41:33 2022

@author: admin
"""

class Rectangle:
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth
    def area(self):
        a=self.l*self.b
        return a
v=Rectangle(12,13)
print(v.area())