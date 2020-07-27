import math
for _ in range(int(input())):
    x,AC=map(int,input().split())
    Radius=AC/math.sin(math.radians(x))
    print(round(Radius/2,6))
