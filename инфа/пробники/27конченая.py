n=int(input())
a=[0]*120
max1=0
max2=0
k=0
for i in range(n):
    x=int(input())
    k=x%120
    if a[k]<x:
        a[k]=x
    if x+a[(120-k)%120]>(max1+max2) and a[(120-k)%120]>x:
        max1=a[(120-k)%120]
        max2=x
print(max1,max2)