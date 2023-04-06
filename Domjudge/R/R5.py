n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
def inverti(a,pos):
    if(pos<len(a)//2):
        k=a[pos]
        a[pos]=a[(pos+1)*-1]
        a[(pos+1)*-1]=k
        inverti(a,pos+1)
    return(a)
b=inverti(a,0)
c=''
for i in b:
    c+=str(i)
print(c,end='')
