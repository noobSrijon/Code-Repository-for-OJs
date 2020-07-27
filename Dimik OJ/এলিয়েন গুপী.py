for i in range(int(input())):
    a=float(input())
    day=0
    for i in range(int(a)):
        if a<=1:
            print(day,"days")
            break
        else:
            a=a/2
            day+=1
            
