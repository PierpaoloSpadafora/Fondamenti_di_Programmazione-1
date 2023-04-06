a=[]

def output(l1):
    ris=''
    for i in l1:
        ris+=str(i)
    print(ris)
    print(len(ris),end='')


def inputa():
    while(True):
        a.append(int(input()))
        if(a[-1]<0):
            break
    return(a)

a=inputa()

lis1=[]
lis2=[]
c=0


if( not(len(a)==1 and a[0]<0)):
    for i in range(c,len(a)-1):
        #print('c:',c,'a[i]',a[i],'a[i+1]',a[i+1])
        if(a[i]<=a[i+1]):
              lis1.append(a[i])
        else:
            lis1.append(a[i])
            c=i+1
            break
        
    while(c<len(a)-1):
        #print(c<len(a)-1,c,len(a)-1)
        for i in range(c,len(a)-1):
            #print('c:',c,'a[i]',a[i],'a[i+1]',a[i+1])
            if(a[i]<=a[i+1]):
                lis2.append(a[i])
            else:
                lis2.append(a[i])
                c=i+1       
                break
        if(len(lis1)<len(lis2)):
            lis1=list(lis2)
        lis2.clear()
        

    output(lis1)
else:
    print('Empty',end='')
