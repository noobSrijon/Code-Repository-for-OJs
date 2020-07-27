A=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]
a=str(input())
x=int(input())
a=a.lower()
if " " in a:    
    a=list(a.split(" "))
for i in range(1,int(len(a)+1)):
    if i>x:
        v=A[A.index(a[i])]
        a.replace(a[i],v)
print(a)
    
