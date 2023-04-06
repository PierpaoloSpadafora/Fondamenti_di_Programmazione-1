
def vprim(n):
    if(n>1):
        ris=True
        for i in range(2,n):
            if(n%i==0):
                ris=False
    else:
        ris=False
    return ris


for i in range(100):
    print(i,' - ',vprim(i))
