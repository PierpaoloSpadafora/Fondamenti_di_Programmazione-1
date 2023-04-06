s=False
cre=False
ris=True
a=[]
c=0
d=0


while(True):
    a.append(int(input()))
    if(a[-1]==0):
        a.pop()
        break
    
if(len(a)>2):        
    c=a[0]
    for i in range(1,len(a)):
        d=a[i]
        if(  not(c<d)  ):
            break
        else:
            c=a[i]

    pos=a.index(d)-1


    for i in range(0,pos-1):
        if( not ( a[i]<a[i+1] ) ):
            ris=False
            break


    for i in range(pos,len(a)-1):
        if( not( a[i]>a[i+1] ) ):
            ris=False
            break
else:
    ris=False
        



if(ris):
    print('SI',end='')
else:
    print('NO',end='')

