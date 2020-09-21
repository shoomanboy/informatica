n=int(input())
sum=0
min=0
for i in range (n):
    x=int(input())
    sum+=x
    if (min==0 or x<min) and x%3!=0
        min=x
if sum%3!=0:
    print(n,sum)
else :
    print(n-1,sum-min)