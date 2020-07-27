x=1
for _ in range(int(input())):
    a,b,c=map(list,input().split())
    if c[0]=="+":
        print("Case {}: {}".format(x,a[0]+b[0]))
    if c[0]=="-":
        print("Case {}: {}".format(x,int(a[0])-int(b[0])))
    if c[0]=="%":
        print("Case {}: {}".format(x,int(a[0]%b[0])))
    if c[0]=="/":
        print("Case {}: {}".format(x,int(a[0]/b[0])))
    if c[0]=="*":
        print("Case {}: {}".format(x,a[0]*b[0]))
    x=x+1
    a.clear()
    b.clear()
    c.clear()
