from random import randint
from random import seed

seed(0)
g=True
CU=0
CPC=0
v=''
def US(x):
    return {
        1: 'hai giocato sasso' ,
        2: 'hai giocato carta' ,
        3: 'hai giocato forbice' ,
    }[x]
def PC(x):
    return {
        1: 'il PC ha giocato sasso',
        2: 'il PC ha giocato carta',
        3: 'il PC ha giocato forbice',
    }[x]
def inputa():
    a=int(input("Inserisci la giocata del primo giocatore (1: sasso, 2: carta, 3: forbice):"))
    return a

p=True

while(g):
    while(True):
        a=inputa()    
        if(a>0 and a<4):
            break
    print(US(a))
    b=randint(1, 3)
    print(PC(b))
    if(a==b):
        print('Pari:')
        print(CU,CPC,sep='-')
    elif((a==1 and b==3)  or  (a==2 and b==1) or (a==3 and b ==2)):
        CU+=1
        print('Vinci tu:')
        print(CU,CPC,sep='-')
    elif((b==1 and a==3)  or  (b==2 and a==1) or (b==3 and a ==2)):
        CPC+=1
        print('Vince il PC:')
        print(CU,CPC,sep='-')
    if(CU==3):
        g=False
        print('Hai vinto la sfida!')
    elif(CPC==3):
        g=False
        print('Il PC ha vinto la sfida!')

