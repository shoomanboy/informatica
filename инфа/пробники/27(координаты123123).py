n = int(input())
maxX = 0
maxY = 0
for i in range(n):
    c = input().split(' ')
    if int(c[0]) == 0 and int(c[1]) > maxY:
        maxY = int(c[1])
    elif int(c[1]) == 0 and int(c[0]) > maxX:
        maxX = int(c[0])
if maxX * maxY == 0:
    print('')
else:
    print(maxX * maxY / 2)
