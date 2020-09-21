import math
x1,y1,r1,x2,y2,r2=map(,input().split(' '))
d=math.sqrt((x2-x1)**2+(y2-y1)**2)
if x1==x2 and y1==y2 and r1==r2:
    print(-1)
elif d==r1+r2 :
    print(1)
elif d==abs(r2-r1):
    print(1)
elif r1+r2<d:
    print(0)
elif r1+r2>d:
    print(2)
elif x1==x2 and y1==y2 and r1!=r2:
    print(0)
