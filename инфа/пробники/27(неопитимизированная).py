n=int(input())

a=[]
k=0
for i in range(n):
    a[i]=int(input())
for i in range(n-1):
    for j in range(i+1,n):
        if a[i]*a[j]%15!=o:
            k+=1
print(k)
