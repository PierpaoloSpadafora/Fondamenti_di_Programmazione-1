
n=int(input())
m=int(input())
mat=[]
for i in range(n):
    mat.append([])
    for j in range(m):
        mat[i].append(int(input()))


_18=m
for j in range(m):
    for i in range(n):
        if(mat[i][j]==18):
            _18-=1
            break
        
media=0
prova=0
nesami=0
maxesami=nesami
contr=[]
    
for i in range(n):
    for j in range(m):
        if(not(mat[i][j]==0)):
            prova+=mat[i][j]
            nesami+=1
    if(prova>0):
        prova=prova/nesami
    contr.append([])
    if(maxesami<nesami):
        maxesami=nesami
    contr[i].append(int(round(prova)))
    contr[i].append(nesami)
    prova=0
    nesami=0

k=0
pos=0
for i in range(n):
    if(contr[k][1]<contr[i][1]):
        k=i
print(_18, contr[k][0],end='')
