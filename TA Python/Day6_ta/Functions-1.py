# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 14:17:12 2022

@author: admin
"""

# Ass1-----


def accept(name, age):
    return(name, age)


print("Tejas", 22)

# Ass2-----


def func1(name, *marks):
    print(name)
    sum = 0
    for i in marks:
        sum = sum+i
        print(marks)


func1("Tejas", 10000, 100)
func1("Ajinkya", 10000, 100)

# Ass3-----


def calculation(a, b):
    return a+b, a-b


print(calculation(20, 10))

# Ass4-----


def showEmployee(name, salary=900):
    print(name, salary)


showEmployee("Tejas", 1000)
showEmployee("Ramesh",)

# Ass5-----????

# def difname()


def x(a): return a*a


print(x(6))


# Ass6-----

def square():
    
  L = [a for a in range(4, 30) if a%2==0]
  return L
print(square())
  
#Ass7-----
def occurance():
    
 L=[1,2,3,3,3,3,4,5]
 L1=[] 
 for i in L:
        if i not in L1:
             L1.append(i)
 return L1

print(occurance())

#Ass8-----
def Square():
     L3=[(i,i**2) for i in range(1,31)]
     return L3
print(Square())

#Ass9-----

def zip1():
    l1=['r','b','g']
    l2=["red","blue","green"] 
    d=dict(zip(l1,l2))
    return d
print(zip1())

#Ass10-----
def sq():
        
   l=[1,2,3,4,5,6,7,8,9,10]
   l2=l(map(lambda a:a*a,l) 
 
 print(sq())



















  