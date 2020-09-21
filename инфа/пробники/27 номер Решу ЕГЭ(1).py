n=int(input())
count14=0
count7=0
count2=0
count1=0
for i in range(n):
    x=int(input())
    if x%14==0 and x>count14:
        count14=x
    elif x%7==0 and x>count7:
        count7=x
    elif x%2==0 and x>count2:
        count2=x
    elif x%14!=0 and x%7!=0 and x%2!=0 and x>count1:
        count1=x
if (count14*count1)>(count7*count2):
    print('max14=',count14*count1)
elif (count14*count1)<(count7*count2):
    print('max14=',count7*count2)