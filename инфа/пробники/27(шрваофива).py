n=int(input())
a=[0]*120
max1=0
max2=0
for i in range(n):
    x=int(input())
    k=x%120
    if x+a[(120-k)%120]>max1+max2 and a[(120-k)%120]>x :
        max1=a[(120-k)%120]
        max2=x
    if x>a[k]:
        a[k]=x
if max2==0 or max1==0:print('no')
else: print('max1=',max1,'max2=',max2)

