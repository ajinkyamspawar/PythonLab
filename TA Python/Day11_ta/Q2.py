no=int(input("enter the number"))
fact=1
lst=[]
for i in range(1,no+1):
    fact=fact*i
    print(i,fact)




def factorial():
    
    no=int(input("enter the number"))
    fact=1
    lst=[]
    for i in range(1,no+1):
        fact=fact*i
        lst.append(fact)
    return(lst)    

print(factorial())
