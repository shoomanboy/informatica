import math
a=[]
s=0
print('введите x y')
for i in range(3):
    a.append(list(map(int,input().split(' '))))
print(a)
s=(abs((a[1][0]-a[0][0])*(a[2][1]-a[0][1])-(a[2][0]-a[0][0])*(a[1][1]-a[0][1])))/2
print('S=',s)