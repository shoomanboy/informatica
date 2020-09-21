n=int(input())
a=list(map(int, input().split(' ')))
d,m=map(int,input().split(' '))
count1=0
count=0
if n==1 and a[0]==d:
    print(1)
else:
    for i in range(n-m+1):
        for j in range(i,i+m):
            count+=a[j]
        if count==d:
            count1+=1
        count=0
    print(count1)