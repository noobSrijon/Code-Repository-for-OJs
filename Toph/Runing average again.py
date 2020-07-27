z=int(input())
A=[int(x) for x in input().split()]
x=0
y=1
for i in A:
    x+=i
    v=x/(y)
    #print(x)
    if int(v)==v:
        print(int(v))
    else:
        print("%.10f"%v)
    y+=1
