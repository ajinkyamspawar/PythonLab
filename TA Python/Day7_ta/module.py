# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 15:21:35 2022

@author: admin
"""

class emp:
    pass
#0======
e=emp()
print(type(emp))
print(type(id(e)))

#1=====

class emp:
    def __init__(self, eno='0', name='nAM'):
        print('Constructor')
        self.eno=eno
        self.name=name
e=emp(50,"Tejas")
#e=emp()
print(e.eno,e.name)

#1=====

    