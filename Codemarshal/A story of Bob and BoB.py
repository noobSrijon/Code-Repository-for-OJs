for i in range(int(input())):
    a,b,c,d,e=map(int,input().split())
    if a/2<b+c+d+e:
        print("Yes")
    else:
        print("No")
