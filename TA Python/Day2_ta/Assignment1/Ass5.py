a,b,c=input("Enter Numbers to find minimum").split()
a=int(a)
b=int(b)
c=int(c)
if(a<b) and (a<c):
    print("a is the smallest number")
elif(b<c) and(b<a):
    print("b is the smallest")
else:
    print("c is the smallest number")
    
