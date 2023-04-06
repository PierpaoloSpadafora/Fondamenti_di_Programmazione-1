def findseq(mat,c):
    if((len(mat))<2):
        return c
    elif(len(mat)==2):
        if(mat[0]+1==mat[1]):
            return c+1
        else:
            return c
    else:
        seq=[]
        inseq=False
        for i in range(len(mat)-1):
            if((mat[i+1]-1)==mat[i]):
                seq.append(mat[i])
                inseq=True
            else:
                if(inseq):
                    seq.append(mat[i])
                    c+=1
                break        
        return(findseq(mat[i+1:],c))            
mat=[]
while(True):
    a=input()
    if(a=='*'):
        break
    else:
        mat.append(int(a))
c=0
a=findseq(mat,c)
print(a,end='')










