import random
a=random.randint(1,30)
for _ in range(int(input())):
    A=str(input())
    B=int(input())
    if A=="multiply":
        a=a*B
    elif A=="add":
        a==a+B
    elif A=="subtract":
        a=a-B
    elif A=="divide":
        a=a/B
print(a)
