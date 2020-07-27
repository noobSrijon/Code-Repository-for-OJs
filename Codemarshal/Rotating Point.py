import math
for i in range(int(input())):
    a,b,c=map(int,input().split())
    r=((a-0)**2+(b-0)**2)**0.5
    x=r*(math.cos(math.radians(c)))
    y=r*(math.sin(math.radians(c)))
    
    print("Case {}: {} {}".format(i+1,x,y))
    
