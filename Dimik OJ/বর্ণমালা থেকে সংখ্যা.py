B=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for i in range(int(input())):
    a=str(input())
    a=list(a)
    A=[]
    for j in a:
        A.append(str(B.index(j)+1))
    print("".join(A))
    A.clear()
        
