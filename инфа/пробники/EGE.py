x=0
n=20
s=0
a=[]
for i in range(n):
    a.append(int(input()))
for i in range(n):
    if a[i]%2!=0:
        x+=1
        s+=a[i]
print('колличество=',x,'среднее ариф.=',s/x)