import math
print('Введите коэффициенты для кв уравнения ax^2+bx+c')
a,b,c=list(map(int,input().split(' ')))
d=b**2-4*a*c
if d==0:
    x=(-b)/(2*a)
elif d<=0:
    print('корней нет')
elif d>0:
    x1=(-b+math.sqrt(d))/(2*a)
    x2=(-b-math.sqrt(d))/(2*a)
    print('x1=',x1,'x2=',x2)