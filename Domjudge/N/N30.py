s=False
alph='abcdefghijklmnopqrstwxyzABCDEFGHIJKLMNOPQRSTWXYZ'
alfmai=''
a=[]
while(True):
    a.append(input())
    if(a[-1]=='*'):
        break
    elif(len(a)>1):
        if( (a[-1] in alph) and (a[-1] in alph) and (a[-1]==a[-2]) ):
            s=True
if(s):
    print('SI',end="")
else:
    print('NO',end="")
