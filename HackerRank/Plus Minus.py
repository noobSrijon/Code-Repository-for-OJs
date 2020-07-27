neg=0
pos=0
zer=0
c=int(input())
A=[int(x) for x in input().split()]
for i in A:
    if i >0:
        pos+=1
    elif i == 0:
        zer+=1
    elif i <0:
        neg+=1
p=pos/len(A)
n=neg/len(A)
z=zer/len(A)
print("%.6f" % p )
print("%.6f" % n)
print("%.6f" % z)
