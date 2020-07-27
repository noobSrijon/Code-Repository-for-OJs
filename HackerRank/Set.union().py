a=int(input())
A=[int(x) for x in input().split()]
b=int(input())
B=[int(x) for x in input().split() ]
print(len(set(A).union(set(B))))
