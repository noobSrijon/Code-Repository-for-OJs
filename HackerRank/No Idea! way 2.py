n,m=map(int,input().split())
a=[int(x) for x in input().split()]
A=set([int(x) for x in input().split()])
B=set([int(x) for x in input().split()])
hap=0
for i in a:
    if i in A:
        hap+=1
    elif i in B:
        hap-=1
    else:
        pass
print(hap)
