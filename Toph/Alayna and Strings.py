a=str(input())
x,y=0,0
for i in a:
    if i.isupper():
        x+=1
    elif i.islower():
        y+=1
print(x,y)
