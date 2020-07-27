A=[]
for i in range(int(input())):
    a=str(input())
    A.append(list(a))
    A=list(*A)
    x=0
    print("Case {}:".format(i+1))
    for j in A:
        X=A[0:x+1]
        X=''.join(X)
        print(X)
        x=x+1
    A.clear()
