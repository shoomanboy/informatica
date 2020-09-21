n=int(input())
a=[0]*n
for i in range(n):
    x=int(input())
    y=5-x%5
    if y<3 and x>40:
        a[i]=x+y
    elif x<38 or y>=3:
        a[i]=x
    elif 38<=x<=40:
        a[i]=40
for i,item in enumerate(a):
    print(item)