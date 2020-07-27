x=0
for i in range(int(input())):
    a=int(input())
    a=str(a)
    for i in a:
        if i=="1":
            x+=2
        elif i=="2":
            x+=5
        elif i=="3":
            x+=5
        elif i=="4":
            x+=4
        elif i=="5":
            x+=5
        elif i=="6":
            x+=6
        elif i=="7":
            x+=3
        elif i=="8":
            x+=7
        elif i=="9":
            x+=6
        elif i=="0":
            x+=6
    print(x,"leds")
    x=0
