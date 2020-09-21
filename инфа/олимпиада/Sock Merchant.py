n=int(input())
a=list(map(int,input().split(' ')))
b=[0]*100
s=0
for i in range(n):
    k=a[i]%100
    b[k]+=1
for i in range(100):
     s+=b[i]//2
print(s)