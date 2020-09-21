A_spisok=input()
B_spisok=input()
ap=0
bp=0
a=A_spisok.split(' ')
b=B_spisok.split(' ')
for i in range(3):
    a[i]=int(a[i])
    b[i]=int(b[i])
    if a[i]>b[i]:
        ap+=1
    elif a[i]<b[i]:
        bp+=1
print(ap,bp)
