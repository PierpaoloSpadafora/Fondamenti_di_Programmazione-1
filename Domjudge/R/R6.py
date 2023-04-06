

def rico(n,mat,t,c):
    s=0
    angolo=mat[n-1-t][t]
    for i in range(n-t):
        s+=mat[i][t]
    for i in range(n-t):
        s+=mat[n-1-t][i+t]
    s-=angolo
    c+=1
    t+=1
    if(s%angolo==0):
        if(c==n-1):            
            return(True)
        else:
            return(rico(n,mat,t,c))
    else:
        return(False)

n=int(input())

mat=[]
for i in range(n):
    mat.append([])
    for j in range(n):
        mat[i].append(int(input()))


a=rico(n,mat,0,0)



if(a):
    print('SI',end='')
else:
    print('NO',end='')

    

