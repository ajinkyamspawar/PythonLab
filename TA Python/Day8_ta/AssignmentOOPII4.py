# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 10:16:23 2022

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
        

class Employee(Person):
    
    def __init__(self,pid,pname,emailid,mobno,dept,desg,sal):
        super().__init__(pid,pname,emailid,mobno)
        self.dept=dept
        self.desg=desg
        self.sal=sal
    
    def getEmployee(self):
        return self.getEmployee
    
    def setEmployee(self):
        return  self.setEmployee
    
    def calculateNetSal(self):
        netsal=self.sal+10/100*self.sal+15/100*self.sal-5/100*self.sal
        return netsal
        
    
    def display(self):
        super().display()
        print(self.dept,self.desg,self.sal)
    print("in Employee")    
    
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


e=Employee(100,"Tarun","xyz@gm.com",98000000000,"Science","Professor",450000)
print(e.calculateNetSal())
