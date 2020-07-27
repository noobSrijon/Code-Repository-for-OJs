n, m = map(int, input().split())

s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))

p1 = set(s1)
p2 = set(s2)

ans = p1 | p2
res = list(ans)
res.sort()

print(*res)
