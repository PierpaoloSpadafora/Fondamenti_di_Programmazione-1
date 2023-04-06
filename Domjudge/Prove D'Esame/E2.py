n=int(input())
mat=[]
col=[]
row=[]
cons=0
success=0
for i in range(n):
    mat.append([])
    for j in range(n):
        mat[i].append(int(input()))
for i in range (n):
    col.append(int(input()))
for i in range (n):
    row.append(int(input()))
for i in range(n):
    som=0
    for j in range(n):
        if(not(mat[j][i]==0)):
            som+=1
    if(som==col[i]):
        success+=1
        
for i in range(n):
    som=0
    for j in range(n):
        if(not(mat[i][j]==0)):
            som+=1
    if(som==row[i]):
        success+=1

if(success==n*2):
    print('SI',end='')
else:
    print('NO',end='')














