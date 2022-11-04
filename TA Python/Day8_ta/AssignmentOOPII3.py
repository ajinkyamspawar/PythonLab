# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 09:56:10 2022

@author: admin
"""

class Person:
    
    def __init__(self,pid,pname,emailid,mobno):
        self.pid=pid
        self.pname=pname
        self.emailid=emailid
        self.mobno=mobno
      
    def display(self):
        print(self.pid,self.pname,self.emailid,self.mobno)  

class Member(Person):
    
    def __init__(self,pid,pname,emailid,mobno,membertype,amtPaid):
        super().__init__(pid,pname,emailid,mobno)
        self.membertype=membertype
        self.amtPaid=amtPaid
        
    def getMember(self):
        return self.getMember
    
    def setMemeber(self):
        return self.setMember
    
    def display(self):
        super().display()
        print(self.membertype,self.amtPaid)

m=Member(101,"Vinay","y@gmail.com",810000000,"Permanent",45.50)
m.display()

    