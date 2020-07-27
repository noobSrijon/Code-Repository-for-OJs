A=[]
a,b=map(int,input().split())
for i in range(a):
    A.append(i%10)
print(A.count(b))
