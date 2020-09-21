n=int(input())
a=[0]*126
max1=0
max2=0
k=0
for i in range(n):
    x=int(input())
    k=x%126
    if x>a[k]:
        a[k]=x
    if x+a[(126-k)%126]>max1+max2 and a[(126-k)%126]>x:
        max1=a[(126-k)%126]
        max2=x
print(max1,max2)
