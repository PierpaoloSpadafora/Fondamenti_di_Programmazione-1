
"""
PRE-TEST
2)Data in input una sequenza di numeri interi positivi terminati da ".",
stampare i numeri in posizione dispari tante volte
quanto vale il numero precedente, per esempio se l'input era:

1
2
3
4
5
6
.
il programma stampava (senza spazi aggiuntivi): 
244466666
"""

def InputMat():
    mat=[]
    while(True):
        a=input()
        if(a=='.'):
            break
        else:
            mat.append(int(a))
    return mat

def ComponiOutput(mat):
    stri=''
    for i in range(1,len(mat),2):
        print(mat[i-1])
        for j in range(mat[i-1]):
            stri+=str(mat[i])
    return stri

def Main():
    mat=InputMat()
    risultato=ComponiOutput(mat)
    print(risultato,end='')

Main()





