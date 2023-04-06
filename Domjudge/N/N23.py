a=''
l='aeiou'
t=False
while(True):
    a=input()
    if(a =='*'):
        break
    elif(a in l):
        if len(a)>0:
            t=True


            
if(t):
    print('ALMENO 1 VOCALE',end='')
else:
    print('NESSUNA VOCALE',end='')
