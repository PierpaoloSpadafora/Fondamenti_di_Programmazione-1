a=[]
b=[]
sel=False
primo=''
disg=False
ctr=True

while(True):
    a.append(input())
    if(a[-1]=='.'):
        a.pop()
        break
while(True):
    b.append(input())
    if(b[-1]=='.'):
        b.pop()
        break

for i in a:
    for j in b:
        if (i==j and sel==False):
            primo=i
            sel=True

for i in a:
    if(i in b):
        disg=True
for i in b:
    if(i in a):
        disg=True



if(not(disg)):
    print('DISGIUNTE',end='')
else:
    print(primo,end='')
