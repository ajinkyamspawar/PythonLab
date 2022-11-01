
#Ass1-----
d={'name':"Ajya", 'age':29}
print(d)

#Ass2-----

d={'name':"Ajya", 'age':29}
d1={'a':1,'b':2}
d2=d.update(d1)
print(d)

#Ass3-----

d={x:x*x*x for x in range(1,10)}
print(d)

#Ass4-----

d={1:10,2:20,3:30}
t=1
for i in d.values():
    t=t*i
print(t)  
  
#Ass5----=-

d={1:10,2:20,3:30}
a=int(input(":Enter Key"))
del d[a]
print(d)

#Ass6-----Also try using pop take variable to store location

sampleDict={"name":"Ramu", 'age':25, "state":"Goa"}
s=sampleDict.setdefault("location","Goa")
del sampleDict["state"]
print(sampleDict)

#Ass7------
l=[1,2,3]
l1=[4,40,5]
d=dict(zip(l,l1))
print(d)

#Ass10-----

people={"Arham":"Blue","Monika":"Red","Lisa":"Yellow", "Vinod":"Purple", "Jenny":"Pink"}
print(len(people))   #10--1

people["Lisa"]="white"
print(people)   #10--2 

del people["Jenny"]
print(people)   #10--3

l=sorted(people.keys())
print(l)
for i in l:
    print(i,people[i])      #10--4
    
    