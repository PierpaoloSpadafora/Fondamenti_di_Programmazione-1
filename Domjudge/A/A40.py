a=[]
b=[]
media=0
while(True):
    a.append(int(input()))
    if(a[-1]==-50):
        a.pop()
        break

if(len(a)<1):
    print('VUOTA',end='')
else:
    for i in a:
        media+=i
    media=media//len(a)
    for i in a:
        if(i>media):
            b.append(i)
    print(min(b),end='')
