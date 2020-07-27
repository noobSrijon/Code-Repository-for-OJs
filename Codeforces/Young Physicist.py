x=0
for i in range(int(input())):
    A=[int(x) for x in input().split()]
    x+=sum(A)
if x==0:
    print("YES")
else:
    print("NO")
