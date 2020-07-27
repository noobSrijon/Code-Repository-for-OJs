x,y=0,0
for i in range(int(input())):
    a=int(input())
    X=[]
    for i in range(a):
        X.append(int(input()))
    if len(X)>0:
        A=list(range(1,max(X)+5))
    else:
        A=list(range(1,5000))
    v=int(input())
    dif=list(set(A)-(set(X)))
    dif=[str(i) for i in dif]
    A="".join(dif)
    A=list(A)
    
    print(A[v-1])
