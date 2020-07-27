for i in range(int(input())):
    a,b=map(int,input().split())
    A=list(range(2,b+1))
    for i in A:
        for j in range(i+i,b+2,i):
            if j in A:
                A.remove(j)
            else:
                continue
    print(A)
    B=list(range(2,b+1))
    B=[x1 - x2 for (x1, x2) in zip(A,B)]
    X=[]
    for i in A:
       for j in B:
            if i%j==0:
               X.append(j)
            else:
                pass
            
    print(B)
    print(len(X))
