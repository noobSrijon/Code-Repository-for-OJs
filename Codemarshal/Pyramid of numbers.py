def numpat(n): 

    num = 1
  
 
    for i in range(0, n): 
     
 
        num = 1
      
 
        for j in range(0, i+1): 
        
 
            print(num, end=" ") 
         
 
            num = num + 1
      
 
        print("\r") 
 
for i in range(int(input())):
	n = int(input())
	print("Case {}:".format(i+1))
	numpat(n)
