g=int(input())
a=list(map(int,input().split(' ')))
c_max=0
max1=a[0]
min1=a[0]
c_min=0
for i,item in enumerate(a):
    if item>max1:
        c_max+=1
        max1=item
    elif item<min1:
        c_min+=1
        min1=item
print(c_max,c_min)



