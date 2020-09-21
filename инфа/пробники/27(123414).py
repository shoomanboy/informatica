
n = int(input())
s = 0
for i in range(n):
    x = int(input())
    if x%2!=0 and x%3!=0:
        m1+=1
    if x%2==0 and x%3!=0:
        m2+=1
    if x%2!=0 and x%3==0:
        m3+=1
    if x%6==0:
        m6+=1
print(m6*(m3+m1)+m2*m3)
print(s)