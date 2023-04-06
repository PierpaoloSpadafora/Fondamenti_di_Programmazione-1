n=int(input())
a=True
for x in range(2,n):
    if(n%x)==0:
        a=False
if(a):
    print('SI',end='')
else:
    print('NO',end='')
