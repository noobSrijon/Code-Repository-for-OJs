A=[int(x) for x in input().split()]
max_sum=max_yet=A[0]
for i in A[1:]:
    max_sum=max(i,max_sum+i)
    max_yet=max(max_yet,max_sum)
print(max_yet)
