a=input()
a=a.split(' ')
for i,item in enumerate(a):
    a[i]=int(item)
d1=max(a)
d2=min(a)
print(sum(a)-d1,sum(a)-d2)
