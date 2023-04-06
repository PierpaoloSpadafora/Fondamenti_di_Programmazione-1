x=int(input());
n=int(input());
a=0
b=1
prin=""
if(x>0):  
    while (a<n):
        a+=1
        num=int(input());
        if(num%2==0 and num<x):        
            prin=prin+ str(num)
else:
     while (a<n):
        a+=1
        num=int(input());
if( len(prin) >0):
    print(int(prin),end='')
