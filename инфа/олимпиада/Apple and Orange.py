st=input().split(' ') # dlinna doma
ab=input().split(' ') # koordinats yablon' u orange  (x)
mn=input().split(' ') # kollichestvo yablock u oranges
m=input().split(' ') # koordinat padeniya yablock
n=input().split(' ') # koordinat padeniya oranges'
count_m=0
count_n=0
for i in range(2):
    st[i]=int(st[i])
    ab[i]=int(ab[i])
    mn[i]=int(mn[i])
for i,item in enumerate(m):
    m[i]=int(item)
for i,item in enumerate(n):
    n[i]=int(item)
for i,item in enumerate(m):
    if st[0]<=item+ab[0]<=st[1]:
        count_m+=1
for i,item in enumerate(n):
    if st[0]<=item+ab[1]<=st[1]:
        count_n+=1
print(count_m)
print(count_n)

