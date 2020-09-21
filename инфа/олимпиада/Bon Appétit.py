import math
n,k=map(int,input().split(' '))
b=list(map(int,input().split(' ')))
fullcost=int(input())
g=(sum(b)-b[k])//2
if g==fullcost:
    print('Bon Appetit')
else:
    x=fullcost-g
    print(x)