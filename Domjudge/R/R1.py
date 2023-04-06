n=int(input())

def rico(n):
    if(n==0):
        return(2)
    else:
        return(3*(n+1)*rico(n-1))

a=rico(n)
print(a,end='')
