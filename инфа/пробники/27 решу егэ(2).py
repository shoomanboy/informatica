a=[]
n=70
j=0
x=0
for i in range(n):
    a.append(int(input()))
for i in range(n):
    if a[i]%7==0 and a[i]>=49 :
        j+=a[i]
for i in range(n):
    if a[i]%7==0 and a[i]>=49:
        a[i]=j
    print(a[i])
    