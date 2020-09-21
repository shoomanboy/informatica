n=int(input())
a=[0]*6
min1=10001
minp=1000001
for i in range(6):
    a[i]=int(input())
for i in range(6,n):
    x=int(input())
    k=x%6
    if a[k]<min1:
        min1=a[k]
    if min1*x<minp:
        minp=min1*x
    a[k]=x
print(minp)