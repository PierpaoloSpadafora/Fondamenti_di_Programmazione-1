a=[]

for i in range(26):
    a.append(input())

n=int(input())

b=[]
for i in range(n):
    b.append(int(input()))

ris=''

for i in b:
    if(i<26):
        ris+=a[i]
if(len(ris)>0):
    print(ris,end='')
