a=input().split(' ') # x1, u1, x2, u2
d1=0
d2=0
count=1
for i,item in enumerate(a):
    a[i]=int(item)
d1=a[0]+a[1]
d2=a[2]+a[3]
if d1<d2 and a[1]<a[3]:
    print('NO')
elif d2<d1 and a[3]<a[2]:
    print('NO')
else:
 while d1!=d2:
     d1+=a[1]
     d2+=a[3]
     if d1!=d2:
         continue
     if d1==d2 :
         print('YES')
         break
     count+=1
