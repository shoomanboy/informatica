a=list(map(str,input().split(' ')))
b=[]
k=str
for i,item in enumerate(a):
    a[i]=a[i].swapcase()
n=len(a)
for i in range(n//2):
    a[i],a[n-i-1]=a[n-i-1],a[i]
b=' '.join(a)
print(b)
