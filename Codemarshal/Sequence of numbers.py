for _ in range(int(input())):
    q=int(input())
    A= [int(x) for x in input().split()]
    if A[1]-A[0] == A[2]-A[1]:
        print(A[len(A)-1]+(A[1]-A[0]))
    else:
        
        print(int(A[len(A)-1]*(A[1]/A[0])))
        
