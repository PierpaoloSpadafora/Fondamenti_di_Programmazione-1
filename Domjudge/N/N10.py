num= int(input())


n=str(num)
a=0
lung=len(n)
ninv=""
while(a<lung):
    Clun=(lung-1)-a
    a+=1
    ninv=ninv+str(n[Clun])

    
ninv=int(ninv)

print(num-ninv, end="")

