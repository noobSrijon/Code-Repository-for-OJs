A=int(input())
x=0
for i in range(1,A):
    if A%i==0:
        x=x+1
    else:
        continue
print(x)
