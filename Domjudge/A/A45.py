
"""
a=input()
if(a.isidentifier()):
    print('SI',end='')
else:
    print('NO',end='')
    
"""
while(True):
    m=input()

    l=("0","1","2","3","4","5","6","7","8","9")

    if m.startswith(l) or len(m)==0 or " " in m:
        print('NO',end='')
    else:
        print('SI', end='')

