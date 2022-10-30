# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 14:06:42 2022

@author: admin
"""
#Ass1-----
s1="maharashtra"
s1=s1.replace('a','$')
print(s1)


#Ass2-----
a="Chinchwad"
b=int(input())
c=a[0:b]
d=a[b+1:]
print(a)
print(c+d)

#Ass3-----
a= "aeiouAEIOU"
b=input()
cnt=0
for i in b:
    if i in a:
        cnt=cnt+1
print(cnt)

#Ass4-----
a=input()
a=a.replace(' ','-')
print(a)

#Ass5-----

b=input()
cnt=0
for i in b:
    cnt=cnt+1
print(cnt)


#Ass6-----
a=input()
b=a[1::2]
print(b)

#Ass7-----
a="ChAnDrApUR"
cnt=0
for i in a:
    if i.islower():
        cnt=cnt+1
print(cnt)

cnt1=0
for i in a:
    if i.isupper():
        cnt1=cnt1+1
print(cnt1)


#Ass8-----
a=input()
b=a[::-1]
if a==b :
    print("It is a Palinrome")
else:
    print("It is not a palindrome")
    
    
#Ass9-----
a="Rajasthan"
b=a[:2]
c=a[7:]
print(b+c)

#Ass10-----
a=input("Enter a String")
b=input("Enter a character to check")
if a.startswith(b):
    print("Yes it starts")
else:
    print("Does not Start")
#Need to write logi for case sensitive
    
#Ass11-----
name=str(input("Enter Name"))
age=int(input("Enter Age"))
salary=float(input("Enter Salary"))
print("Hello,{},you are{} years old and getting salary{}".format(name,age,salary))
print("Hello,{2},you are{1} years old and getting salary{0}".format(name,age,salary))
print("Hello,{a},you are{n} years old and getting salary{s}".format(n=name,a=age,s=salary))



#Ass12----

s="AlwaysThinkPosiTive"
#1
a=s[5]
print(a)
print("-----")
#2
print("-----")
b=s[10]
print(b)
#3
print("-----")
c=s[5:8]
print(c)
print("-----")
#4
d=s[6:9]
e=d[::-1]
print(e)
print("-----")
#5
print(s)
#6
print("-----")
f=s[2:]
print(f)
print("-----")
#7
g=s[0:8]
print(g)
print("-----")
#8
h=s[::-1]
print(h)
print("-----")
#9
i=s[-5:-2]
print(i)
print("-----")
#10
j=s[0:17]
print(j)
print("-----")
#10
k=s[-6:]
print(k)
print("-----")
#10
l=s[::2]
print(l)
print("-----")
#11
m=l[::-1]
print(m)
print("-----")

#Ass13-----
s="The Quick brownfox jumps over the lazy dOG"
print(s)

#Ass14-----

print(s.lower())
print(s.upper())
print(s.title())
print(s.swapcase())
print(s.capitalize())













