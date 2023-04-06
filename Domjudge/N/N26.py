k=0
a=[]
g=False
s=True
while(s):
    a.append(input())
    if(a[-1]=='*'):
        a.pop()
        break
    elif(len(a)>1):
        if( (a[-1].isupper() and a[-2].isupper()) or ( a[-1].islower() and (a[-1] == a[-2]) ) ):
            k+=1
if(k>0):
    print('SI',end='')
else:
    print('NO',end='')




