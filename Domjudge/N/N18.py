a=[]
k=0
s=True
t=False
while(s):
    a.append(input())
    if(len(a)>1):
        if(a[-1]=='k' and a[-2]=='o'):
            break
print(len(a)-2,end='')
