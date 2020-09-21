a=[0]*117
max1=0
max2=0
n=int(input())
for i in range(n):
    x=int(input())
    k=x%117
    if a[(117-k)%117]>x and a[(117-k)%117]+x>max1+max2:
        max1=a[(117-k)%117]
        max2=x
    if x>a[k]:
        a[k]=x
print(max1,max2)
