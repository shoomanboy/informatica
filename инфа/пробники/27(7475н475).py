n=int(input())
a=[0]*5
count13=0
x13=0
for i in range(5):
    a[i]=int(input())
for i in range(5,n):
    x=int(input())
    k=x%5
    if a[k]%13==0:
        count13+=1
    if x%13==0:
        x13+=i-4
    else:
        x13+=count13
    a[k]=x
print(x13)
