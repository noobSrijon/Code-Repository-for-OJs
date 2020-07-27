for x in range(int(input())):
    a,b=map(int,input().split())
    A=list(range(2,b+1))
    for i in A:
        for j in range(i+i,b+2,i):
            if j in A:
                A.remove(j)
            else:
                continue
    X=0
    for i in range(a,b,2):
        for n in A:
            if i%n==0:
                X+=1
            else:
                continue
    print(X)

    A.clear()
    
    X=0
    
