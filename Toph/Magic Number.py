def isPrime(n): 
    if n <= 1: 
        return False
    for i in range(2, int(n)): 
        if n % i == 0: 
            return False; 
  
    return True
for i in range(int(input())):
    a=(int(input()))**.5
    if isPrime(a):
        print("YES.")
    else:
        print("NO.")
