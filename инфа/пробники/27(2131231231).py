a = [0] * 9
n = int(input())
s = 0
k = 0
for i in range(n):
    x = int(input())
    a[x % 9] += 1
s = (a[0] * (a[0] - 1)) // 2
for i in range(1, 5):
    k+= a[i] * a[9 - i]
print(s + k)

