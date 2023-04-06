"""

PRE-TEST
1) Dati in input 4 numeri interi positivi A,B,C,D ( in cui A<=B; C<=D),
si scriva un programma che verifichi
se negli intervalli da A a B e poi da C a D ci sia ALMENO UN
numero "amico di 2" IN COMUNE.
Un "amico di 2" sarebbe un numero ottenuto dalla somma di un multiplo di 2 e 1
(per esempio17=16+1, oppure 5=4+1).

"""

def elencaamici2(a,b):
    mat=[]
    for i in range(b-a+1):
        if( ( (a+i)-1) % 2 == 0 ):
            mat.append(a+i)
    return(mat)

def verificaamicocomune(m1,m2):
    for i in range(len(m1)):
        if(m1[i] in m2):
            return(True)
        
def output(ris):
    if(ris):
        print('SI',end='')
    else:
        print('NO',end='')
      
def main():
    a=int(input())
    b=int(input())
    c=int(input())
    d=int(input())
    mat1=elencaamici2(a,b)
    mat2=elencaamici2(c,d)
    output(verificaamicocomune(mat1,mat2))



main()
