q=int(input())
A=set(map(int,input().split()))
for i in range(int(input())):
    eval('A.{0}({1})'.format(*input().split()+['']))
print(sum(A))
