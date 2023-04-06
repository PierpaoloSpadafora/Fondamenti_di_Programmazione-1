PrimoMese= 500
SecondomoMese= round((PrimoMese+(PrimoMese*2)/100)-5)
TerzoMese= round((SecondomoMese+(SecondomoMese*2)/100)-5)
print("PRIMO MESE: " + str(PrimoMese))
print("SECONDO MESE: " + str(SecondomoMese))
print("TERZO MESE: " + str(TerzoMese), end='')
