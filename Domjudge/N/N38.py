mat=[]
nummagg=[]
media=[]
for i in range(100):
    mat.append(int(input()))
    if(mat[-1]<-50 or mat[-1]>50):
        nummagg.append(mat[-1])
    elif(mat[-1]>-50 or mat[-1]<50):
        media.append(mat[-1])
out=''
if(len(nummagg)>0):
    for j in range(len(nummagg)):
        out+=str(nummagg[j])
    print(out,end='\n')
else:
    print('VUOTO1',end='\n')
out2=0
if(len(media)>0):
    for j in range(len(media)):
        out2+=media[j]
    out2=round(out2/len(media),6)
    print(out2,end='')
else:
    print('VUOTO2',end='')






    
