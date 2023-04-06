a=int(input())
b=int(input())


def isPrime(num):
    a=True
    if(num>1):
        for i in range(2,num):
            if (num%i)==0:
                a=False
    return a


if(isPrime(a) and isPrime(b)):
    if( abs(a-b)==2 ):
        print('gemelli',end='')
    else:
        print('non gemelli',end='')
else:
    print('non entrambi primi',end='')
