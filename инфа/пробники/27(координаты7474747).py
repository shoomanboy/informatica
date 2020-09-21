n = int(input())
maxy1 = 0
maxx1 = 0
miny1 = 0
maxy2 = 0
maxx2 = 0
miny2 = 0
s1 = 0
s2 = 0
for i in range(n):
    c = input().split(' ')
    if int(c[0]) == 0 and int(c[1]) != 0:
        if int(c[1]) > maxy1 and int(c[1]) > 0:
            maxy1 = int(c[1])
        if miny1 < int(c[1]) < maxy1 and int(c[1]) > 0:
            miny1 = int(c[1])
        if maxy2 > int(c[1]) and int(c[1]) < 0:
            maxy2 = int(c[1])
        if int(c[1]) < 0 and maxy2 < int(c[1]) < miny2:
            miny2 = int(c[1])
    if int(c[0]) > 0 and int(c[1]) > 0 and abs(int(c[0])) > abs(maxx1):
        maxx1 = abs(int(c[0]))
    elif int(c[0]) < 0 and int(c[1]) < 0 and abs(int(c[0])) > abs(maxx2):
        maxx2 = abs(int(c[0]))
s1 = ((maxy1 - miny1) * maxx1) / 2
s2 = ((miny2 - maxy2) * maxx2) / 2
if s1 > s2:
    print('s1=', s1)
else:
    print('s2=', s2)
