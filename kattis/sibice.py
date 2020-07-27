A=list(input())
for _ in range(int(A[0])):
    for x in A:
        v=int(input())
        if v%int(x) == 0:
            print("NE")
        else:
            print("DA")
        del v
