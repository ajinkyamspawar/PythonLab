# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 08:55:12 2022

@author: admin
"""
#Ass1-----
l=[1,2,3,4,5]
sum=0
for i in l:
    sum=sum+i
    avg=sum/len(l)
print(sum)
print(avg)

#Ass2-----
l=[-1,-2,-3,4,6,8,9,11,13]
sum=0
sum1=0
sum2=0
for i in l:
    if i<0:
        sum=sum+i
    if i>0 and i%2!=0:
        sum1=sum1+i
    if i>0 and i%2==0:
         sum2=sum2+i
print(sum)
print(sum1)
print(sum2)

#Ass3-----
l=[4,6,8,9,11,13]
for i in l:
    if i>0 and i%2==0:
        l2=[i]
        e=max(l2)
    else :
       l1=[i]
       o=max(l1)
print(e)
print(o)


#Ass4------
#wd=input("Enter days")
#l=[wd]
#print(l)

l=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
for i in range(0,len(l)):
   a=print(l[i][0:3], end=" ")
   
#Ass4-----one more way
l=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
for i in l:
    a=i[:3]
    print(a, end=" ")

#Ass5-----
l=[1,2,3,1,2,3,1,2,3]
a=l.count(1)
print(a)

#Ass6-----
l=[1,2,3,4,5,6,13,24,4,21]

print(max(l))

#Ass6-----one more way
l=[1,2,3,4,5,6,13,24,4,21]
a=l.sort()
print(max(l)


#As7-----
l=[1,2,3,4,5,6,13,24,4,21]
print(l[8])

#Ass8----
l=[4,6,8,9,11,13]
a=[]
b=[]
for i in l:
    if i>0 and i%2==0:
        a.append(i)
    else:
        b.append(i)
        
print(a)       
print(b)

#Ass9-----onemoreway by using append
l1=[1,2,3,5,8,9]
l2=[10,12,11]
l1.extend(l2)
print(l1)
l1.sort()
print(l1)

#Ass10-----
l1=[1,2,3,5,8,9]
l1[0],l1[-1]=l1[-1],l1[0]
print(l1)


#Ass11-----
l1=[1,2,3,5,8,9,3,2,3,9]
b=[]
for i in l1:
    if i not in b:
        b.append(i)
print(b)


#Ass12------
l1=[1,2,3,5,8,9]
a=l1.index(9)
print(a)


#Ass13-----
a=int(input("Enter your choice"))
while(a<9)
    if a==1:
    

#Ass14-----

L1=[ x**2 for x in range(11,21)]
print(L1)

#Ass15------
L1=[ x for x in range(1,1000) if x%7==0]
print(L1)

#Ass16------


L1=[ x for x in range(1,1000)if '5' in str(x)]
print(L1)

#Ass17-----
wordlist=["this","is","an","example"]
L=[x[0:1] for x in wordlist]
print(L)

#Ass18-----
wordlist=["this","is","an","example"]
L=[(x,len(x)) for x in wordlist]
print(L)















































