x=int(input())
y=int(input())
a=0
for x in range(x,y+1):
    if((x%2)!=0):
        a+=x
print(a,end='')
