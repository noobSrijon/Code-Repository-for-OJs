a,b,c,d,v,t=map(int,input().split())
distance=((c-a)**2+(d-b)**2)**0.5
t=distance/v
print("%0.6f"%t)
