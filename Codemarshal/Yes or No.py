p=int(input())
a=int(input())
k=int(input())
x=0
y=a
for i in range(1,k+1):
   x=(a+i)
   y=y*x
y=y*a
if y%p == 0:
    print("yes")
else:
    print("no")
