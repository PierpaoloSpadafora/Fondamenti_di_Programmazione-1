a=[]
h=0
m=0
s=0
t=0
k=0
l=1
while(True):
    a.append(input())
    if(a[-1]=='0'):
        a.pop()
        break

for x in range(0,len(a)):
    if( (a[x] != 'h' and a[x] != 'm' and a[x] != 's') and (len(a[x])>0 and a[x]!=' ') ):
        t=int(a[x])
    elif(a[x] == 'h'):
        h=3600*t
        t=0
        k=k+h
    elif(a[x] == 'm'):
        m=60*t
        t=0
        k=k+m
    elif(a[x] == 's'):
        s=t
        t=0
        k+=s
print(k,end='')
