n = 10
a = []
j = 100
for i in range(n):
    a.append(int(input()))
for i in range(n):
    if 9 < a[i] < 100 and a[i] % 10 == 3 and a[i] < j:
        j = a[i]
if j == 100:
    print('пошел нахуй саня')
else:
    print(j)
