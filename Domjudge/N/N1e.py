def cal(Mese,Canone,Interesse):
    Mese=Mese-Canone
    return(Mese+((Mese/100)*Interesse))
PrimoMese = int(input())
Canone = int(input())
Interesse = int(input())
SecondoMese= round(cal(PrimoMese,Canone,Interesse))
TerzoMese= round(cal(SecondoMese,Canone,Interesse))
print("PRIMO MESE:",PrimoMese)
print("SECONDO MESE:",SecondoMese)
print("TERZO MESE:",TerzoMese,end="")
