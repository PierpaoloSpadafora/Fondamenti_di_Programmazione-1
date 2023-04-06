n=int(input())

costo=5

if(n>80):
    if(n<140):
        n=n-80
        costo=5+(0.10*n)
    elif(n<190):
        n=n-140
        costo=11+(0.07*n)
    else:
        n=n-190
        costo=14.5+(n*0.05)

costo=round(costo, 3)
print(costo,end='')
    
