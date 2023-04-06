CostoMat=int(input())
NOre=int(input())

Prezzo=CostoMat+(NOre*40)

if(Prezzo<100):
    Prezzo=100
    
print(Prezzo,end='')
