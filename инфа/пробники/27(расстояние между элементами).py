n = int(input())
a = [0] * 8
max1 = 0
max2 = 0
for i in range(8):
    x = int(input())
    a[i] = x
for i in range(8, n):
    x = int(input())
    k = i % 8
    if a[k] > max1:
        max1 = a[k]
    if x > max2:
        max2 = x
    a[k] = x
print('max2=', max2, 'max1=', max1)
print(max2 * max1)
