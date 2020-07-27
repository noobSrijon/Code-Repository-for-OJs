for _ in range(int(input())):
    a=int(input())
    if a%2==0:
        c=str(a+1)[::-1]
        print(c)
    else:
        c=str(a-1)[::-1]
        print(c)
                
