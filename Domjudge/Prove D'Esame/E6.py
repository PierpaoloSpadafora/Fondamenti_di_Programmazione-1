n=int(input())
x=int(input())
a=[]
for i in range(n):
    a.append([])
    for j in range(2):
        a[i].append(int(input()))
ColA=[]
ColB=[]
for i in range(n):
    ColA.append(a[i][0])
    
for i in range(n):
    ColB.append(a[i][1])
    
pos=ColB.index(2019)
if(ColA[pos]==0):
    ris='SI'
else:
    ris='NO'
AMB=max(ColB,key=ColB.count)
print(str(AMB)+' '+ris,end='')

