import math
print('введите x y для центра первой окружности')
o1=[]
o1.append(list(map(int,input().split(' '))))
print('введите x y для центра второй окружности')
o2=[]
o2.append(list(map(int,input().split(' '))))
print('введите радиусы 1 и 2 окружностей')
r1,r2=map(int,input().split(' '))
d=math.sqrt(abs((o2[0][0]-o1[0][0])**2-(o2[0][1]-o1[0][1])**2))
if d>r1+r2:
    print('Каждая из окружностей лежит вне другой')
elif d==r1+r2:
    print('Внешнее касание двух окружностей')
elif d==abs(r1-r2):
    print('Внутреннее касание двух окружностей')
elif abs(r1-r2)<d<r1+r2:
    print('Окружности пересекаются в двух точках')
elif d<abs(r1-r2):
    print('Одна из окружностей лежит внутри другой')
