n=int(input())
cont=0
j=1
for i in range(n-1):
    cont+=j
    j+=2
cont=cont*2+j
print(cont,end='')

