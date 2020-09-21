a=input()
a=a.split(':')
b=[]
a[0]=int(a[0])
b=list(a[2])
if b[2]=='P' and b[3]=='M':
    a[0]=a[0]+12
    if a[0]==24:
        a[0]=0
if (b[2]=='P' and b[3]=='M') and a[0]==12 and a[1]=='00' and (b[1] and b[2])=='0':
    a[0]='12'
if (b[2]=='P' and b[3]=='M') and a[0]==12 and (a[1]!='00' or b[1]!='0' or  b[2]!='0') :
    a[0]=0
if (b[2]=='A' and b[3]=='M') and a[0]==12 and (a[1]!='00' or b[1]!='0' or  b[2]!='0') :
    a[0]=0
if (b[2]=='A' and b[3]=='M') and a[0]<=12:
    a[0]=str(a[0])
if (b[2]=='P' and b[3]=='M') and 1<=a[0]<=10:
    a[0]=str(a[0])
    a[0]='0'+a[0]
b.remove(b[2])
b.remove(b[2])
if a[0]==0:
    a[0]='00'
b=b[0]+b[1]
a[2]=b
print(':'.join(map(str,a)))