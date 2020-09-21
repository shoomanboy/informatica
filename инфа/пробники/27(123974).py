n=int(input())
m1=0
m2=0
m5=0
m10=0
s=0
for i in range(n):
    x=int(input())
    if x%2==0 and x%5==0:
        m1+=1
    elif x%2==0 and x%5!=0:
        m2+=1
    elif x%2!=0 and x%5!=0:
        m5+=1
    elif x%2!=0 and x%5==0:
        m10+=1
s=m1*m5+m2*m10+m10*m1
print(s)
