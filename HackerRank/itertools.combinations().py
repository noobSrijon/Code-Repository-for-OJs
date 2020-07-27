from itertools import combinations as cn
a,b=map(str,input().split())
b=int(b)
for i in range(1,int(b)+1):
    for j in cn(sorted(a),i):
        print("".join(j))
