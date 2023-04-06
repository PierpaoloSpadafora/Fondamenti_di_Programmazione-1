pques=[]
for i in range(8):
    pques.append(int(input()))
studenti=[]
for i in range(4):
    k=''
    for i in range(9):
        k+=input()
        k+=' '
    studenti.append(k)
soglia=int(input())

"""
##input di prova

pques=[2,3,5,1,7,4,2,5]
studenti=['A1 10 4 0 3 1 5 2 5','A2 3 5 3 9 2 6 0 3','A3 2 4 10 6 3 7 0 1','A4 8 6 2 4 4 8 3 1 ']
soglia=100

"""

superati=[]
for i in range(4):
    voto=0
    read=studenti[i].split(' ')
    matricola=read[0]
    for j in range(len(pques)):
        voto=voto+int(read[j+1])*pques[j]
    if(voto>soglia):
        superati.append([voto, matricola])
        print(matricola,voto)
print(len(superati),superati[superati.index(max(superati))][1],superati[superati.index(min(superati))][1], end='')
