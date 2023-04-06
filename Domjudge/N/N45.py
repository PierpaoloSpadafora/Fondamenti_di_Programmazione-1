ad=0
bd=0
a=''
b=''
n=input()
n=list(n)
n = [int(i) for i in n]
m=n[:]
while len(m)>0:
    ad=max(m)
    a+=str(ad)
    m.remove(max(m))

while len(n)>0:
    bd=min(n)
    b+=str(bd)
    n.remove(min(n))
a=int(a)
b=int(b)
print(a-b,end='')
