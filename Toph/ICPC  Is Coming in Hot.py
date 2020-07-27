a=int(input())
A=[int(x) for x in str(a)] 
print(max(A,key=A.count))
