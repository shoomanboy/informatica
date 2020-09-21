n = int(input())
max19 = 0
max1 = 0
max38 = 0
max2 = 0
for i in range(n):
    x = int(input())
    if x % 2 == 0 and x % 19 == 0 and x > max38:
        max38 = x
    elif x % 2 != 0 and x % 19 == 0 and x > max19:
        max19 = x
    elif x % 2 == 0 and x > max2:
        max2 = x
    elif x % 2 != 0 and x > max1:
        max1 = x
if (max38 + max2) > (max19 + max1):
    if max38 != 0 and max2 != 0:
        print('max38=', max38, '  max2=', max2)
else:
    if max19 != 0 and max1 != 0:
        print('max19=', max19, '  max1=', max1)
if max38 == 0 or max2 == 0:
    if max19 == 0 or max1 == 0:
        print('0 0')
