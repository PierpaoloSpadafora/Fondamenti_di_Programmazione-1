m=int(input())
n=int(input())
mat=[]
for i in range(m):
    mat.append([])
    for j in range(n):
        mat[i].append(int(input()))
giudici=[]
cantanti=[]        
for i in range(m):
    c=0
    for j in range(n):
       if(mat[i][j]>5):
           c+=1
    giudici.append(c)
for i in range(n):
    c=0
    for j in range(m):
        c+=mat[j][i]
    cantanti.append(c)
giudice = len(giudici)- 1 - giudici[::-1].index(max(giudici))
cantante = len(cantanti)- 1 - cantanti[::-1].index(min(cantanti))
print(giudice,cantante,sep=' ',end='')

