A=int(input())
x=1
A=[]
for i in range(int(input())):
    while len(A)>=10:
        a=int(input())
        a=list(a)
        for i in a:
            if i not in A:
                A.append(i)
            else:
                continue
        print("Case #{}: {}".format(x,a))
        a*=(i+1)
    x+=1
