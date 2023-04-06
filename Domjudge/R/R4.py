x=int(input())
n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
    
def rico(x,a,somm):
    c=0
    for i in range(len(a)):
        if(a[i]==x):
            a[i]=0
            c+=1
    somm+=c
    if(c==0):
        print(somm,end='')
    else:
        rico(c,a,somm)
c=0
somm=0
rico(x,a,somm)




