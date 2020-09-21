n = int(input())
a = [0] * 4
k = 0
min1 = 1001
min2 = 1001
for i in range(4):
    x = int(input())
    a[i] = x
for i in range(4, n):
    x = int(input())
    k = i % 4
    if a[k] < min1:
        min1 = a[k]
    if x < min2:
        min2 = x
    a[k] = x
print('min1=', min1, 'min2=', min2)
print(min1 + min2)
