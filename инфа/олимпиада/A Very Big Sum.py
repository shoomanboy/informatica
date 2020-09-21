import math
n=int(input())
array=input()
a=array.split(' ')
for i, item in enumerate(a):
    a[i]=int(item)
for i in a:
    print(i,end=' ')
print()
print(a)