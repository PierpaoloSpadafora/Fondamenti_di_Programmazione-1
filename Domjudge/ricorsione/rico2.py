n=int(input())
mat=[]
for i in range(n):
    mat.append(int(input()))
def rico(mat,pos):
    ris='NO'
    if(n%2==0):
        if(pos<len(mat)/2):
            if(mat[pos]==mat[pos+(len(mat)//2)]):
                ris='SI'
                rico(mat,pos+1)
            else:
                ris='NO'
    else:
        ris='NO'
    return(ris)
print(rico(mat,0),end='')
