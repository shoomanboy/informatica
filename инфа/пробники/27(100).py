n=int(input())
count2=0
count11=0
count22=0

for i in range (n):
    x=int(input())
    if x%2==0:
        count2+=1
    elif x%11==0:
        count11+=1
    elif x%22==0:
        count22+=1
print((count22*(count22-1))//2+count22*(n-count22)+count2*count11)