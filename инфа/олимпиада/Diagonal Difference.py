import math
n = 3
d1=0
d2=0
a = [[11, 2, 4],
     [4, 5, 6],
     [10, 8, -12]]
for i in range(n):
    d1+=a[i][i]
    d2+=a[i][n-i-1]
print(abs(d1-d2))




