n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
ris=False
if((n%2)==1):
    ris=False
else:
    c=n//2
    b=a[c:]
    a=a[:c]
    if(a==b):
        ris=True
if(ris):
    print('SI',end='')
else:
    print('NO',end='')
