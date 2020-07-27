def getMissingNo(A): 
    n = len(A) 
    total = (n + 1)*(n + 2)/2
    sum_of_A = sum(A) 
    return total - sum_of_A
for i in range(int(input())):
    A=[int(x) for x in input().split()]
    C=A[0]
    A.remove(A[0])
    print(int(getMissingNo(A)))
