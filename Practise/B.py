A=int(input())
B=[]
if A%2==0:
    for i in range(2,A+1,2):
        B.append(i)
else:
    for i in range(2,A+1,2):
        B.append(i)
print(sum(B))
