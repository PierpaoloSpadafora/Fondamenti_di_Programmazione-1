frase=input()

def farfalla(frase):
    farf=''
    vocale='aeiou'
    for i in frase:
        if(i in vocale):
            farf+=i+'f'+i
        else:
            farf+=i
    return(farf)

def invertidametà(farf):
    finale=''
    finale=farf[len(farf)//2:len(farf)] + farf[0:len(farf)//2]
    return(finale)

farf=farfalla(frase)
finale=invertidametà(farf)


print(finale,end='')
