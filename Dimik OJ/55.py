def mul(A):
    x=1
    for i in A:
        x=x*i
    return x
A=[]
x=int(input())
for _ in range(x):
    A.append(int(input()))
A=A[::-1]
X=[]
for i in A:
    A.remove(i)
    X.append(mul(A))
    A.append(i)
print(X)
    
