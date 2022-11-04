# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 08:45:17 2022

@author: admin
"""

#Ass1------

class Person:
    
    def __init__(self,pid,pname,emailid,mobno):
        self.pid=pid
        self.pname=pname
        self.emailid=emailid
        self.mobno=mobno
        
    def display(self):
        print(self.pid,self.pname,self.emailid,self.mobno)
        
i=Person(100,"Tarun","xyz@gm.com",98000000000)
i.display()
#print(i.pid ,i.pname,i.emailid,i.mobno)--use this print when no display method 
                                          #used


        