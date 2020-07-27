def samerem(A):
    B=[]
    for i in A:
        if i not in B:
            B.append(i)
    return B
a,b,c=map(int,input().split())
A=[int(x) for x in input().split()]
B=[int(x) for x in input().split()]
v=0
X=[]
for i in min(A,B):
    for j in max(A,B):
        if (i+j)%c==0:
            X.append([i,j])
        else:
            pass
print(len(samerem(X)))
