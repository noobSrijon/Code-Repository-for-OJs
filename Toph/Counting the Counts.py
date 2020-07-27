q=int(input())
a=0
A=[int(x) for x in input().split()]
for i in A:
    if i>=80:
        a+=1
print(a)
