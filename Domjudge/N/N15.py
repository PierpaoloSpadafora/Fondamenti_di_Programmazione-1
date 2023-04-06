a=[]
k=0
s=True
while(s):
    a.append(int(input()))
    if(len(a)>=3):
        if(a[-1]==a[-2] and a[-1]==a[-3]):
            if(a[-1]!=9):
                k+=1
            else:
                break
print(k,end='')
