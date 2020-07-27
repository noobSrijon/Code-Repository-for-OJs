A=""
for i in range(int(input())):
    a=str(input())
    A=a
    A=sorted(list(A))
    for x in A:
        print("{} = {}".format(x,A.count(x)))
    
