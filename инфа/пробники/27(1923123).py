max7=0
max1=0
x=int(input())
while x!=0:
    x=int(input())
    if x%7==0 and x%49!=0 and x>max7:
        max7=x
    elif x%7!=0 and x%49!=0 and x>max1:
        max1=x
if (max7*max1)==0:
    print('1')
r1=int(input())
if max7*max1==r1
    print('значениея совпали')
else:
    print('значениея не совпали')




