a=[]
k=0
s=True
t=False
while(s):
    a.append(input())
    if(a[-1]=='*'):
        break
    else:
        if(len(a)>1):
            if(a[-1] == a[-2]):
                t=True
                
if(t):
    print('SI',end='')
else:
    print('NO',end='')

