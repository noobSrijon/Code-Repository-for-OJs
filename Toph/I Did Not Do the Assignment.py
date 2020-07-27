num = int(input())
if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           for i in range(num):
               print("I DID NOT DO THE ASSIGNMENT.")
           break
   else:
       print("NO PUNISHMENT")
else:
    for i in range(num):
        print("I DID NOT DO THE ASSIGNMENT.")
