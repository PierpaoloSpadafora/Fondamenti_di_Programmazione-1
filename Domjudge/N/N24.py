a=[]
k=0
g=False
voc='aeiou'
cons='bcdfghjklmnpqrstvwxyz'
s=True
t=True
l=False
while(s):
    a.append(input())
    if(a[-1]=='.'):
        a.pop()
        break
    elif(len(a)==1):
        if(len(a[-1])>0):
            if( (a[-1] in voc) or (a[-1] in cons) ):
                k+=1
                
    elif(len(a)>1):
        if(len(a[-1])>0 and len(a[-2])>0):
            if( (a[-1] in voc and a[-2] in voc) or (a[-1] in cons and a[-2] in cons) ):
                g=True
                k+=1
                if(not l):
                    l=True
                    k-=1
if(g):
    k+=1
print(k,end='')
