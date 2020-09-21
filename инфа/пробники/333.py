a = []
n = 10
min = -1
max = 0
sum = 0
sred1 = 0
sred2 = 0
for i in range(n):
    a.append(int(input()))
for i in range(n):
    sum += a[i]
    if (a[i] < min) or min == -1:
        min = a[i]
    if a[i] >= max:
        max = a[i]
print('min', min, '  max', max)
sred1 = (min + max) / 2
sred2 = sum / n
print('sred1-sred2=', sred1 - sred2)
