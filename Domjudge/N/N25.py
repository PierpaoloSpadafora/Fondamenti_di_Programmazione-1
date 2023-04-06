a=[]
k=0
s=True
t=False

a.append(input())
k+=int(a[0])
if(k==0):
    print(k,end='\n')
while(s):
    a.append(input())
    if(a[-1]=='0' and a[-2]=='0'):            
        break
    else:
        if(a[-1]=='0'):
            print(k,end='\n')
            k=0
        else:
            k+=int(a[-1])


