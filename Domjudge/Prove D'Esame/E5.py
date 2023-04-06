mat=[]
while(True):
    a=input()
    if(a!='*'):
        mat.append(a)
    else:
        mat.append('A')
        break
seq=''
prov=''
for i in range(len(mat)-1):
    if(ord(mat[i])>=ord(mat[i+1])):
        prov+=mat[i]
    else:
        prov+=mat[i]
        if(len(seq)<len(prov)):
            seq=prov
            prov=''
        else:
            prov=''            
if(len(seq)<len(prov)):
            seq=prov
if(len(seq)<2):
    print('0',end='')
else:
    print(ord(seq[0])-ord(seq[-1])-1,end='' )
















