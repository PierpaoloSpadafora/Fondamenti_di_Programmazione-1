a=input()

pa=0
pc=0
bp=False
nps=True
opened=0

for i in range(0,len(a)):
    if(a[i]=='('):
        opened+=1
    elif(a[i]==')'):
        opened-=1
    if(opened<0):
        break

if(opened==0):
    bp=True




lun=len(a)
for i in range(0,lun-1):
    if(a[i]=='('):
        if(i<lun-1):
            if(a[i+1]==')'):
                nps=False



    
if(bp):
    print("ok1")
else:
    print("no1")


if(nps):
    print("ok2")
else:
    print("no2")



