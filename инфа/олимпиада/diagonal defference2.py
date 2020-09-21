import math
n=int(input())
b=[]
d1=0
d2=0
for i in range(n):
    a=[]
    a=input()
    a=a.split(' ')
    for j in range(n):
        a[j]=int(a[j])
    b.append(a)
for i in range(n):
    d1+=b[i][i]
    d2+=b[i][n-1-i]
print(abs(d1-d2))