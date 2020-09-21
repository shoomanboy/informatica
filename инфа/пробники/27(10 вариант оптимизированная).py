n=int(input())
a=[0]*6
count=0
count13=0
for i in range(6):
    a[i]=int(input())
for i in range(6,n):
    x=int(input())
    k=i%6
    if a[k]%13==0:
        count13+=1
    if x%13==0:
        count+=i-5
    else:
        count+=count13
    a[k]=x
print(count)