int(input())
A=[int(x) for x in input().split()]
z=0
x=1
for i in A:
    if x%2==0:
        pass
    else:
        z+=i
    x+=1
print(z)
