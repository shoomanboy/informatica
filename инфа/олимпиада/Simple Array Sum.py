n = int(input())
stroka = input()
a = stroka.split(' ')
for i,item in enumerate(a):
    a[i] = int(item)
print(sum(a))
