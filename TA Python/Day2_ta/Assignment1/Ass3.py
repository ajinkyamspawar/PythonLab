s1,s2,s3,s4,s5=input("Enter Marks").split()
s1=int(s1)
s2=int(s2)
s3=int(s3)
s4=int(s4)
s5=int(s5)


marks=s1+s2+s3+s4+s5
if marks>450:
    print("Grade A")
elif marks>400:
    print("Grade First class")
elif marks>350:
    print("Grade Second class")
else:
    print("Fail")



          
