b=1
c=0
while (b!=5):
    b=int(input());
    if(b!=5 and b%5==0):
        c=1
if(c==1):
    print('ALMENO 1',end='')
else:
    print('NESSUNO',end='')
    
