def Matrice(N,M):
    mat=[]
    for i in range(N):
        mat.append([])
        for j in range(M):
            mat[i].append(0)
    return(mat)

def InputComandi(mat,penna,n,m):
    j=0
    coms=0
    while(j<100):
        coms=int(input())
        if(coms==9):
            coms.pop()
            break
        else:
            Muoviti(mat,coms,penna,n,m)
        j+=1

def visualizzaPavimento(pavimento, dim):
    for i in range(dim):
        for j in range(dim):
            if pavimento[i][j]==1:
                print("*",end="")
            else:
                print("-",end="")
        print()

def direzione(x):
    return{
        3:'es',
        4:'ws',
        5:'sd',
        6:'nd',
        }[x]

def spostamento(mat,direzione,penna,n,m):
    passi=input("passi?")
    print()
    
    if(direzione=='es'):
        if(penna):
            if((20-(m+1))>=passi):
                for i in range(0,passi):
                    ma=m+i
                    mat[n][ma]=1
            else:
                x=m+passi
                y=x-20
                passi-=y
                for i in range(0,passi):
                    ma=m+i
                    mat[n][ma]=1
        else:
            if((20-(m+1))>=passi):
                for i in range(0,passi):
                    ma=m+i
            else:
                x=m+passi
                y=x-20
                passi-=y
                for i in range(0,passi):
                    ma=m+i
        m=ma


                    
    elif(direzione=='ws'):
        if(penna):
            if((20-(m+1))>=passi):
                for i in range(0,passi):
                    ma=m+i
                    mat[n][ma]=1
            else:
                x=m+passi
                y=x-20
                passi-=y
                for i in range(0,passi):
                    ma=m+i
                    mat[n][ma]=1
        else:
            if((20-(m+1))>=passi):
                for i in range(0,passi):
                    ma=m+i
            else:
                x=m+passi
                y=x-20
                passi-=y
                for i in range(0,passi):
                    ma=m+i    

def Muoviti(mat,comandi,penna,n,m):

    if( comandi[i]>0 and comandi[i]<10  ):
        if(comandi[i]==9):
            break
        if(comandi[i]==8):
            pass
        if(comandi[i]==7):
            visualizzaPavimento(mat, 20)
        if(comandi[i]>2 and comandi[i]<7):
            direzione=direzione(comandi[i])
            
            var=[]

            var=spostamento(mat,direzione,penna,n,m)
            mat=var[0]
            direzione=[]

            
        if(comandi[i]==2):
            penna=True
        if(comandi[i]==1):
            penna=False
    return(mat,penna,n,m)


mat=Matrice(20,20)
#visualizzaPavimento(mat, 20)

penna=True
var=[]
n=0
m=0
InputComandi(mat,penna,n,m )
var=Muoviti(mat,comandi,penna,n,m)
mat=var[0]
penna=var[1]
n=var[2]
m=var[3]

