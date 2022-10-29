a=int(input())
temp=a
rev=0
while a!=0:
    mod=a%10
    rev=rev*10+mod
    a=a//10
   # print(a)
if(rev==temp):
    print("Number is Palindrom")
else:
    print("Number is not Palindrom")
