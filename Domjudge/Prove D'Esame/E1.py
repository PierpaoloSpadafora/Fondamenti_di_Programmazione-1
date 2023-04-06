import string
a=[]
ris=False
global contr
contr=string.ascii_letters+string.digits+'_'


def LeggiLista():
    while(True):
        a.append(input())
        if (a[-1]==':'):
            break
    a.pop()
    return a

    
def ValidaNome(st):
    ris=True
    if(not(st[0].isdigit())):
        for i in range(len(st)):
            if(not(st[i] in contr)):
                ris=False
    else:
        ris=False
    return ris


def ValidaVar(st):
    ris=True
    if(not(st[0].isdigit())):
        for i in range(len(st)):
            if(not(st[i] in contr)):
                ris=False
    else:
        ris=False
    return ris


bab=True
a=LeggiLista()
if(a[0]=='def'):
    if(a[2]=='(' and a[-1]==')'):
        if(ValidaNome(a[1])):
            c=3
            while(c<len(a)-2):
                if(bab==False):
                    break
                if(ValidaVar(a[c]) and a[c+1]==','):
                    c=c+2
                else:
                    bab=False
            if(bab):
                if(len(a)-1>=c+1):
                    if(a[c+1]==')'):
                        ris=True
                else:
                    if(a[c]==')'):
                        ris=True


if(ris):
    print('SI', end='')
else:
    print('NO', end='')

