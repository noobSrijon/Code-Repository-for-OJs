a,b=map(int,input().split())
A=[0 for i in range(a)]
for i in range(b):
    x,y=map(int,input().split())
    X=A[x:]
    for  j in A[:x]:
        X.append(j+y)
A=X
print(X)
    
        
