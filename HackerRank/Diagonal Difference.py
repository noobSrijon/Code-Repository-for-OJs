x=0
n=int(input())
A=[int(x) for x in input() .split()]
B=[int(x) for x in input() .split()]
C=[int(x) for x in input() .split()]
for j in range(n):
    x=A[j]+B[j+1]+C[j+2]
print(x)
