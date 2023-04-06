CostoBigl=float(input())
Sconto=int(input())

def f(x):
    return {
        0: 1,
        1: 10,
        2: 15,
        3: 25,
    }[x]

if(Sconto==0):
    ris=CostoBigl
    ris=round(ris,3)
    print(ris,end='')
else:
    ris=CostoBigl - ((CostoBigl*f(Sconto))/100)
    ris=round(ris,3)
    print(ris,end="")
