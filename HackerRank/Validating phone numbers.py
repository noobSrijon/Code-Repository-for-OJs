for _ in range(int(input())):
    A=int(input())
    A=list(str(A))
    if len(A)==10 and A[0]=="7" or A[0]=="8" or A[0]=="9":
        print("YES")
    else:
        print("NO")
