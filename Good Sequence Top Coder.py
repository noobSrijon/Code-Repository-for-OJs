a=int(input())
A=[int(x) for x in input().split()]
ans=0
for i in A:
    n=A.count(i)
    if n<i:
        ans+=1
    elif n>=i:
        ans+=n-i
print(ans)
