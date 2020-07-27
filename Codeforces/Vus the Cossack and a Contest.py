a,b,c=map(int,input().split())
if a<b and a<c:
    print("Yes")
elif a==b and a==c:
    print("Yes")
elif a<b and a==c:
    print("Yes")
elif a<c and a==b:
    print("Yes")
else:
    print("No")
