y=int(input())
if y%4==0:
    y=str(y)
    y='12.09.'+y
    print(y)
elif y%4!=0:
    y=str(y)
    y='13.09.'+y
    print(y)