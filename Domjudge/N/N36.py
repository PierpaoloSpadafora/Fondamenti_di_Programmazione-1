a=[]
    
for i in range(0,10):
    a.append(int(input()))

x=int(input())
s=True

for i in a:
    if(i%x==0):
        s=False
        break


if(s):
    print('OK',end='')
else:
    print('NO',end='')
