for i in range(int(input())):
    a=str(input())
    b=str(input())
    x=list(a)
    if b in x:
        print("Occurrence of '{}' in '{}' = {}".format(b,a,a.count(b)))
    else:
        print("'{}' is not present".format(b))
