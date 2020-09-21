n = int(input())
a = [0] * 6
maxchet = 1001
maxnechet = 1001
maxchet1 = 1001
maxnechet1 = 1001
s1 = 0
s2 = 0
s3 = 0
for i in range(6):
    a[i] = int(input())
for i in range(6, n):
    x = int(input())
    k = i % 6
    if (a[k] < maxchet and a[k] % 2 == 0):
        maxchet = a[k]
    if (a[k] < maxnechet and a[k] % 2 != 0):
        maxnechet = a[k]
    if x < maxchet1 and x % 2 == 0:
        maxchet1 = x
    if x < maxnechet1 and x % 2 != 0:
        maxnechet1 = x
    a[k] = x
s1 = maxchet * maxchet1
s2 = maxnechet * maxchet1
s3 = maxnechet1 * maxchet
p = min(s1, s2, s3)
print('maxchet=', maxchet, 'maxnechet=', maxnechet)
print('maxchet1=', maxchet1, 'maxnechet1=', maxnechet1)
print(p)
