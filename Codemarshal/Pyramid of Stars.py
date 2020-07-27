A=[]
x=0
for i in range(int(input())):
    a=int(input())
    for j in range(1,a+1):
        S="*"*j
        A.append(S)
    A=''.join(A)    
    print(*A[0:x+1])
    x=x+1
    A.clear()
