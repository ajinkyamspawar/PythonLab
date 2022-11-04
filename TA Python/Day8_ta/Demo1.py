# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 08:16:44 2022

@author: admin
"""


class emp:
    pass
class manager(emp):
    pass

e=emp()
m=manager()

print(isinstance(e,emp))
print(isinstance(m,emp))
print(isinstance(e,manager)) #not istance since employee as parent class cant
# be an instance of child class
print(isinstance(m,manager))

print(issubclass(emp,emp))#same class is a subclass of itself
print(issubclass(emp,manager))
print(issubclass(manager,manager))
print(issubclass(manager,emp))

#------------------------------------------------------------------------------

#Inheritance demo

class emp:
    
    def __init__




