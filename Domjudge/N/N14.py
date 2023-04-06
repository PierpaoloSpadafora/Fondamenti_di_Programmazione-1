a=0
c=''
t=True
while(a!=-1):
    a=int(input())
    if(a!=-1):
        if(a<10 and a>0):
            b=a
            b=str(b)
            c+=b
        else:
            t=False


if(t):
    if(len(c)!=0):
        c=int(c)
        if((c%3)==0):
            print(c)
            print('SI',end='')
        else:
            print(c)
            print('NO',end='')
    else:
        print('VUOTO',end='')
else:
    print('ERRORE',end='')



