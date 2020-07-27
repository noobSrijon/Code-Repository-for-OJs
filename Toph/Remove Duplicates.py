def semrem(a):
    B=[]
    for i in a:
        if i not in B:
            B.append(i)
    return B
def strf(A):
    B=[]
    for i in B:
        B.append(str(i))
    return B
b=1
for i in range(int(input())):
    a=str(input())
    A=[]
    x=a
    x=semrem(x)
    for i in x:
        A.append(a.count(i))
    print("Case #{}".format(b))
    A=strf(A)
    for i in range(len(A)):
        print("{} {}".format(b[x],A[x]))
        
        
        
    b+=1
