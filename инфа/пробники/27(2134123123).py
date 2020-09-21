n=int(input())
count34=0
count2=0
count17=0
count1=0
for i in range(n):
    x=int(input())
    if x%34==0 and x>count34:
        count34=x
    if x%17==0 and x>count17:
        count17=x
    if x%2==0 and x>count2 and x%34!=0:
        count2=x
    if x%2!=0 and x%17!=0 and x>count1:
        count1=x
if count34*count2>count17*count1 and count34*count2!=0:
    print(count34+count2)
elif count17*count1>count34*count2 and count17*count2!=0:
    print(count17+count1)
else: print('0 0')