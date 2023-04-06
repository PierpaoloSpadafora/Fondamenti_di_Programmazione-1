X=int(input())
a=[]
k=0
s=True
if(X==-1):
    s=False
g=False
while(s):
    a.append(int(input()))
    if(a[-1]==-1):
        a.pop()
        break
    else:
        for b in a:
            if(b==0):
                k+=1
            else:
                k=0
            if(k>=X):
                g=True

if(g):
    print('OK',end='')
else:
    print('NO',end='')
            
