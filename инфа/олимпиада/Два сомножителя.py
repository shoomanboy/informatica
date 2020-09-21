k=int(input())
if k==1:
    print(1)
elif k==2:
    print(4)
else:
    n=2**k+2**(k-1)
    print(n)
