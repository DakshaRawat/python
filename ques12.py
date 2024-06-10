n=int(input("enter number"))
sum=0
while n>0:
    m=int(n)%10
    sum=sum+m
    n=n/10
print(sum)