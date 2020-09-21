n=int(input())
a=list(map(int,input().split(' ')))
b=[0]*6
k=0
for i,item in enumerate(a):
    b[a[i]]+=1
k=max(b)
for i,item in enumerate(b):
    if item==k:
        print(i)
        break
