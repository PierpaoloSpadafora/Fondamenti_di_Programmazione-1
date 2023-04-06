n=int(input())
a=[]
for i in range(n):
    a.append([])
    for j in range(n):
        a[i].append(int(input()))

b=[]
ris=True
for i in range(n):
    for j in range(n):
        b.append(a[i][j])
    b_set=set(b)
    if(not(len(b)==len(b_set))):
        ris=False
    b=[]
    
for i in range(n):
    for j in range(n):
        b.append(a[j][i])
    b_set=set(b)
    if(not(len(b)==len(b_set))):
        ris=False
    b=[]

if(ris):
    print('SI',end='')
else:
    print('NO',end='')
