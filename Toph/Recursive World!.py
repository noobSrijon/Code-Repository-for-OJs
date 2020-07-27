for _ in range(int(input())):
    f=int(input())
    if f==0:
        print("1")
    elif f==1:
        print("2")
    else:
        n=f-1
        v=(f*f)+(f*n)+1
        print(v)
    
