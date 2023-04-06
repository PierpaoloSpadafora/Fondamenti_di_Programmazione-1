a=[]
k=0
s=True
t=True
while(s):
    a.append(input())
    if(a[-1]=='.'):
        break
    else:
        if( not(a[-1].isalpha()) ):
            t=False
if(t):
    print('SI',end='')
else:
    print('NO',end='')
