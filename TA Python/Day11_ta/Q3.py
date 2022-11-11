lst=[12, 67, 98, 34]
l=[]
for i in lst:
    mod=i%10
    ret=i//10
    print(mod+ret)
    
    
    
lst=[12, 67, 98, 34]
l=[]
for i in lst:
    sum=0
    for j in str(i):
        sum=sum+int(j)
    l.append(sum)
print(l)    
        
    
    
    
    