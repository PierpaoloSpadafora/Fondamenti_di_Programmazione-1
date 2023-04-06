n=input()
lett='abcdefghijklmnopqrstuvwxyz'
for i in range(len(n)):
    lett=lett.replace(n[i],'')
if(len(lett)==0):
    print('SI',end='')
else:
    print('NO',end='')

    
