n = int(input())
count62 = 0
count31 = 0
count2 = 0
s = 0
for i in range(n):
    x = int(input())
    if x % 62 == 0:
        count62 += 1
    elif x % 31 == 0:
        count31 += 1
    elif x % 2 == 0:
        count2 += 1
s = (count62 * (count62 - 1)) / 2 + count2 * count31 + (n - count62) * count62
print(s)
