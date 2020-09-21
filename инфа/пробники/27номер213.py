a = [0] * 7
n = int(input())
s = 0
k = 0
for i in range(n):
    x = int(input())
    a[x % 7] += 1
s = (a[0] * (a[0] - 1)) // 2
for i in range(1, 4):
    k += a[i] * a[7 - i]
print(s + k)
