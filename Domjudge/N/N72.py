corr=input()
a=[]
for i in range(90):
    a.append([])
    a[i].append(input())
    a[i].append(input())
for i in range(90):
    punt=0
    rispstud=a[i][1]
    for j in range(20):
        if(rispstud[j]=='X'):
            pass
        else:
            if(rispstud[j]==corr[j]):
                punt+=2
            else:
                punt-=1
    a[i][1]=punt
for i in range(90):
    print(a[i][0],a[i][1],sep=' ',end='\n')

