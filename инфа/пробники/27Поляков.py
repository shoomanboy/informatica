max1=0
max2=0
n=int(input())
for i in range (n):
    x=int(input())
    if x%3==1 and x>max1:
        max1=x
    elif x%3==2 and x>max2:
        max2=x
print('значение R')
R=int(input())
if R>(max1+max2):
    print("не пройдено")
else:
    print('пройдено')
