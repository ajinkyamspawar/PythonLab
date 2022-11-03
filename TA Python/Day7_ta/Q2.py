# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 15:55:07 2022

@author: admin
"""

class reverse:
    def __init__(self,sen):
        self.x=sen
    def rev(self):
        a=self.x.split(" ")
        a.reverse()
        d=" ".join(a)
        d=str(d)
        print(d)
sentence=input("Enter Sentence")
b=reverse(sentence)
b.rev()