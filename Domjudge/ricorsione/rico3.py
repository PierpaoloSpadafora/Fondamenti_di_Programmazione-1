n=int(input())
mat=[]
for i in range(n):
    mat.append([])
    for j in range(n):
        mat[i].append(int(input()))
diag=0
for i in range(n):
    diag+=mat[i][n-i-1]

def DiagonaleInversa(mat,rdiag,pos):
    if(pos<len(mat)):
        rdiag+=mat[pos][len(mat)-pos-1]
        return DiagonaleInversa(mat,rdiag,pos+1)
    return rdiag
rdiag=DiagonaleInversa(mat,0,0)
print(diag,rdiag,sep=';',end='')
