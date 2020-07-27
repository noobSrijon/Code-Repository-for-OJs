def multiplyList(myList) : 
    result = 1
    for x in myList: 
         result = result * x  
    return result  
A=[]
a=int(input())
for _ in range(a):
    A.append(int(input()))
x=multiplyList(A)
for i in range(1,a+1):
    print(int(x/i))
