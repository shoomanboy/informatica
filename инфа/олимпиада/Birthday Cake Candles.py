n=int(input())
countMax=0
a=input()
a=a.split(' ')
k=0
for i,item in enumerate(a):
    a[i]=int(item)
    if a[i]>countMax:
        countMax=a[i]
for i,item in enumerate(a):
    if a[i]== countMax:
        k+=1
print(k)
