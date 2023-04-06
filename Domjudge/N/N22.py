a=[]
k=0
s=True
t=False
while(s):
    a.append(input())
    if(a[-1]=='.'):
        break
    else:
        if( a[-1].isalpha() ):
            t=True
if(t):
    print('SI',end='')
else:
    print('NO',end='')
