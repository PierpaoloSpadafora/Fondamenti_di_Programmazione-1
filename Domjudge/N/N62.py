"""
k=int(input())

a=[]
for i in range(k):
    a.append(int(input()))

n=int(input())
m=int(input())

letter=[]
i=0
for k in range(n*m):
    if(len(a)>i):
        letter.append(a[i])
        i+=1
    else:
        i=0
        letter.append(a[i])
        i+=1
print(letter)

mat=[]       
for i in range(n):
    mat.append([])
    for j in range(m):
        mat[i].append(0)

"""


def posiz(inn,inm,n,m,pos):
    safn=inn
    safm=inm
    n=n+inn
    m=m+inm
    while(inm<m):
        pos.append([inn,inm])
        inm+=1
    inm-=1
    inn+=1
    while(inn<n):
        pos.append([inn,inm])
        inn+=1
    inn-=1
    inm-=1
    while(inm>safm):
        pos.append([inn,inm])
        inm-=1
    inn-1
    while(inn>safn):
        pos.append([inn,inm])
        inn-=1

    
    return(pos)




        
    
        
pos=[]        
n=2
m=3

print(posiz(2,2,n,m,pos))    










