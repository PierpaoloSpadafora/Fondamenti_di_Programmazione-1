a=int(input())
b=int(input())
def rico(a,b):
    if(a==0 or b==0):
        return 0
    else:
        resto=a%b
        if(resto==0):
            return b
        else:
            a,b=b,resto
            return rico(a,b)
ris=rico(a,b)
print(ris,end='')
