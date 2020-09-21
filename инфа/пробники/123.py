a = []
n = 9
j = 0
k = 0
for i in range(n):
    a.append(int(input()))
k = -1
for i in range(1, 8):
    if (a[i]) < (a[i - 1]) and (a[i]) < (a[i + 1]) and ((a[i] < k) or (k == -1)):
        k = a[i]
if k == -1:
    print('0')
else:
    print(k)
