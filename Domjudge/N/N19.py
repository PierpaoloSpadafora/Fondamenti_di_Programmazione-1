a=[]
k=0
s=True
t=False
while(s):
    a.append(input())
    if(a[-1]=='*'):
        break
    else:
        if(a[-1].isdigit()):
            t=True
if(t):
    print('ALMENO UNA',end='')
else:
    print('NESSUNA',end='')

