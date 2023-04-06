N=int(input())
a=[]
k=0
s=True
t=False


while(s):
    a.append(int(input()))

    if(a[-1]==-1): 
        a.pop()           
        break
    else:
        if(a[-1]<=N):
            k+=1
            if(k>=N):
                t=True
        else:
            k=0

    if(N==0):
        t=True
if(t):
    print('OK',end='')
else:
    print('NO',end='')


