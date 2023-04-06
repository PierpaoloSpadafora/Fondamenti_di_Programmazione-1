def f(x):
    return {
        1: 'INVERNO',
        2: 'INVERNO',
        4: 'PRIMAVERA',
        5: 'PRIMAVERA',
        7: 'ESTATE',
        8: 'ESTATE',
        10: 'AUTUNNO',
        11: 'AUTUNNO',
    }[x]

def spe(x):
    return {
        30: 'INVERNO',
        60: 'PRIMAVERA',
        90: 'ESTATE',
        120: 'AUTUNNO',
        3: 'PRIMAVERA',
        6: 'ESTATE',
        9: 'AUTUNNO',
        12: 'INVERNO',
    }[x]

n=int(input())
if(n<1 or n>12):
    print('MESE NON VALIDO',end='')
else:
    if(n!=3 and n!=6 and n!=9 and n!=12):
        print(f(n), end='')
    else:
        g=int(input())
        if(g>=1 and g<=20):
            n=n*10
        print(spe(n), end='')
        


