lis = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]#[-1, 1, -1, 8,2,2]
lst=[] 
for i in lis:
    if lis.count(i)>1 and i not in lst :#count fuctions uses to count the occurances 
        lst.append(i) 
print(lst )        