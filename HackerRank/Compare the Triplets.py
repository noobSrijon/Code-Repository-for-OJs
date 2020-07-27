A=[int(x) for x in input().split()]
B=[int(x) for x in input().split()]
a=0
b=0
for i in range(len(A)):
    if A[i]>B[i]:
        a+=1
    elif A[i]<B[i]:
        b+=1
    else:
        continue
print(a,b)
