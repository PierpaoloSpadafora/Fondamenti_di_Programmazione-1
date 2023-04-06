def val(x):
    return {
        1: 11,
        2: 2,
        3: 10.5,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
    }[x]

SemeB = int(input())

Seme1g = int(input())

Carta1g = int(input())

Seme2g = int(input())

Carta2g = int(input())



Carta1g = val(Carta1g)  
Carta2g = val(Carta2g)

if(Seme1g==SemeB):
    if(Seme2g==Seme1g):
        if(Carta2g>Carta1g):
            print('VINCE GIOCATORE 2',end='')
        else:
            print('VINCE GIOCATORE 1',end='')
    else:
        print('VINCE GIOCATORE 1',end='')
else:
    if(Seme2g==SemeB):
        print('VINCE GIOCATORE 2',end='')
    else:
        if(Seme2g==Seme1g):
            if(Carta2g>Carta1g):
                print('VINCE GIOCATORE 2',end='')
            else:
                print('VINCE GIOCATORE 1',end='')
        else:
            print('VINCE GIOCATORE 1',end='')

    
    

