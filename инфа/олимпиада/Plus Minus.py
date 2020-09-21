import math
def ostatok(number,count):
    return f"{number:.{count}f}"

n=int(input())
c_positive=0
c_negative=0
c_zero=0
a=input()
a=a.split(' ')
for i,item in enumerate(a):
    a[i]=int(item)
    if a[i]>0:
        c_positive+=1
    elif a[i]<0:
        c_negative+=1
    elif a[i]==0:
        c_zero+=1
print(ostatok((c_positive/n),6))
print(ostatok((c_negative/n),6))
print(ostatok((c_zero/n),6))
