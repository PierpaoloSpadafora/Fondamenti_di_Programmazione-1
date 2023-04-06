def potenza(x,y):
    while(x%y==0):
        x=x/y
    if(x!=1):
        return False
    else:
        return True



a=[]

s=True

while(True):
    a.append(int(input()))
    if(a[-1]==0):
        a.pop()
        break
    
if(len(a)>0):
    for i in a:
        if(not (potenza(i,2)) ):
            s=False
            break

    
if(s):
    print('SI',end='')
else:
    print('NO',end='')

