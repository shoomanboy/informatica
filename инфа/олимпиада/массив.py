a=[]
n=10
k=0
for i in range(n):
    a.append(int(input()))
for i in range(n):
    k+=a[i]
if k%2==0 :
    k=0
    for i in range(n):
        if a[i]%2!=0:
            k+=1
elif k%2!=0:
    k=0
    for i in range(n):
        if a[i]==0:
            k+=1
input("k=",k)
