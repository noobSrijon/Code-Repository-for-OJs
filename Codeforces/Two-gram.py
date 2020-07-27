from itertools import permutations
a=int(input())
a=str(input())
a=list(a)
X=[]
perm=permutations(a,2)
for i in perm:
    X.append("".join(i))
print(max(X,key=X.count))
