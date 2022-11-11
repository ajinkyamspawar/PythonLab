lst= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l=[]

for i in lst:
    m=1
    for j in i:
        m=m*j
        l.append(m)
print(max(l))
 