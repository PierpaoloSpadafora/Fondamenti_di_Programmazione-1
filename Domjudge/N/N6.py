a=int(input())

if((a%4==0)):
    if((a%100==0)):
        if((a%400==0)):
            print('BISESTILE',end="")
        else:
            print('NON BISESTILE',end="")
    else:
        print('BISESTILE',end="")
else:
     print('NON BISESTILE',end="")
