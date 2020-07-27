def tprime(n):
    a=0
    for i in range(1,n):
        if n%i==0:
            a+=1
        else:
            pass
    if a==2:return True
    else:return False
a=int(input())
A=[int(x) for x in input().split()]
for i in A:
    if tprime(i):
        print("YES")
    else:print("NO")
