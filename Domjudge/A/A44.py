a=input()
a=list(a)
s1=0
s2=0
for i in range(0, len(a)//2):
    s1+=int(a[i])
    
for i in range(len(a)//2,len(a)):
    s2+=int(a[i])

if(s1==s2):
    print('FORTUNATO',end='')
else:
    print('SFORTUNATO',end='')
