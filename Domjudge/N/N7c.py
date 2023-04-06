v1=[]
v1.append(int(input()))
if(v1[0]==0):
    print('BALLOTTAGGIO',end='')
else:
    i=0
    while(v1[i]!=0):
        i+=1
        v1.append(int(input()))
    v1.pop()
    l=len(v1)

    av=v1.count(1)
    ap=round((av/l)*100,1)
    bv=v1.count(2)
    bp=round((bv/l)*100,1)
    cv=v1.count(3)
    cp=round((cv/l)*100,1)

    print('1',av,ap)
    print('2',bv,bp)
    print('3',cv,cp)

    if(ap>50):
        print('VINCE 1',end='')
    elif(bp>50):
        print('VINCE 2',end='')
    elif(cp>50):
        print('VINCE 3',end='')
    elif(ap<=50 and bp<=50 and cp<=50):
        print('BALLOTTAGGIO',end='')
