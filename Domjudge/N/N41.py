lis=[0,0,0,0,0,0,0,0,0,0]
rf=0
rn=5
def scegliposto(lis,rf,rn):
    a=input("Digitare 1 per fumatori o 2 per non fumatori:")

    if(a=='1'):
        if(rf<5):
            lis[rf]=1
            rf+=1
        else:
            a=input("Reparto scelto al completo. Si desidera un posto nell'altro reparto (S/N)?")
            if((a=='S' or a=='s') and rn<10):
                lis[rn]=1
                rn+=1
            elif(a=='N' or a=='n'):
                print("Il prossimo volo parte tra 3 ore")
    elif(a=='2'):
        if(rn<10):
            lis[rn]=1
            rn+=1
        else:
            a=input("Reparto scelto al completo. Si desidera un posto nell'altro reparto (S/N)?")
            if((a=='S' or a=='s') and rf<5):
                lis[rf]=1
                rf+=1
            elif(a=='N' or a=='n'):
                print("Il prossimo volo parte tra 3 ore")
    return(lis,rf,rn)


cont=0
bab=scegliposto(lis,rf,rn)
while cont<9:
    cont+=1
    lis=bab[0]
    rf=bab[1]
    rn=bab[2]
    bab=scegliposto(lis,rf,rn)
