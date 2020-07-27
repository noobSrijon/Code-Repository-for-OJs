for i in range(int(input())):
    a=int(input())
    v=0
    for j in range(a):
        v+=float(input())
    print("Case {}: {:.3f}".format(i+1,v/a))
