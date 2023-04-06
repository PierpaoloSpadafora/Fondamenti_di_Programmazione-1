s=input()
n=int(input())

a=[]

for i in range(n):
    a.append(input())

ris=False
for i in range(n):
    for j in range(n):
        if(s==a[i]+a[j]):
            ris=True



if(ris):
    print('OK',end='')
else:
    maggiore=''
    for i in a:
        if(maggiore<i):
            maggiore=i
    minore=a[0]
    for i in a:
        if(minore>i):
            minore=i
    print(maggiore+minore,end='')
