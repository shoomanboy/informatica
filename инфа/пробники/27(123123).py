a = [0] * 10
n = int(input())
s = 0
k = 0
for i in range(n):
    x = int(input())
    a[x % 10] += 1
s = (a[0] * (a[0] - 1)) // 2 + (a[5] * (a[5] - 1)) // 2
for i in range(1, 5):
    k += a[i] * a[10 - i]
print(s + k)
