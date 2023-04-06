n=int(input())
def f(n):
    if(n==0):
        return(2)
    else:
        return((3*(n+1))*f(n-1))
print(f(n),end='')
