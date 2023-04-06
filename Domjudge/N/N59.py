"""
while(True):
    try:
        n=(int(input()))
        if(n<3 or (n%2==0)):
            raise ValueError
        else:
            break
    except ValueError:
        pass
"""
n=int(input())
a=[]

for i in range(0,n):
    a.append([])
    for j in range(0,n):
        a[i].append(int(input()))
"""
a=[[1,0,0,0,0],[0,0,0,0,0],[0,0,1,0,0],[0,0,0,0,0],[0,0,0,0,0]]
for i in range(len(a)):
    print(a[i])
"""
somma=0
croce=0
for i in range(len(a)):
    croce+=a[i][len(a)//2]
for i in range(len(a)):
    croce+=a[len(a)//2][i]
for i in range(len(a)):
    for j in range(len(a)):
        somma+=a[i][j]
croce-=a[len(a)//2][len(a)//2]
somma-=croce
if(croce>somma):
    print('OK',end='')
else:
    print('NO',end='')










