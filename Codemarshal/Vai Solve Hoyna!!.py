c=0
x=1
for i in range(int(input())):
    z=int(input())
    a=str(input())
    b=str(input())
    a=sorted(list(a))
    b=sorted(list(b))
    for i,j in zip(a,b):
        if i==j:
            c+=1
    if c==z:
        print("Case {}: vai problem solve hoy na".format(x))
    else:
        print("Case {}: table e boisha thak solve hobe".format(x))
    
    x+=1
