A=str(input())
print any(c.isalnum()  for c in A)
print any(c.isalpha() for c in A)
print any(c.isdigit() for c in A)
print any(c.islower() for c in A)
print any(c.isupper() for c in A)
        
