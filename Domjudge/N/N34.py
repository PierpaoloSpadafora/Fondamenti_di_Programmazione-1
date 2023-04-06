

x=int(input())
a=[]
for i in range(x):
    a.append(int(input()))
    

i=0
b=[]
c=[]
while(i<len(a)):
    b.append(a[i])
    i+=2
i=1
while(i<len(a)):
    c.append(a[i])
    i+=2
    

ris=True

for i in range(len(b)-1):
    if(b[i]+1>b[i+1]):
        ris=False


for i in range(len(c)):
    if((c[i]%2)==0):
        ris=False


if(ris):
    print('SI',end='')
else:
    print('NO',end='')
