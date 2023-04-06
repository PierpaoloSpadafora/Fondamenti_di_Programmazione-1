
c=0
voc='aeiou'
star='*'
risultato=True
t=0
a=[]
for i in range(100):
    a.append(input())

for vocale in a:
    if(vocale in voc):
        if(t==0):
            star=vocale
            t=1
        elif(t==1 and not(vocale==star)):
            risultato=False
            break


if(risultato):
    print('OK',end='')
else:
    print('ERRORE',end='')
