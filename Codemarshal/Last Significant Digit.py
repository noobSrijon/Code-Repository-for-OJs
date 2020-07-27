A=0
a,b=map(int,input().split())
for i in range(1,a+1):
    if (i%10)==b:
        A+=1
print(A)
