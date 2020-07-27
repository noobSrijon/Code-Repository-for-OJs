for i in range(int(input())):
    a=int(input())
    A=[int(x) for x in input().split()]
    b=int(input())
    B=[int(x) for x in input().split()]
    C=sorted(A+B)
    print(*C)
