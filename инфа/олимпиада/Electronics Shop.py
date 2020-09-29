b, n, m = map(int, input().split(' '))  # b=budget,n=count keyboards,m=count drives
k = list(map(int, input().split(' ')))  # cost of keyboard
d = list(map(int, input().split(' ')))  # cost of drives
price = 0
for i in range(n):
    for j in range(m):
        if k[i] + d[j] > price and k[i] + d[j] <= b:
            price = k[i] + d[j]
        else: price=-1
print(price)
