import itertools
def convert(list): 
    res = sum(d * 10**i for i, d in enumerate(list[::-1])) 
      
    return(res) 

A=itertools.permutations("HACK",2)
A=sorted(A)
A=convert(A)
for i in A:
    new_data = (' '.join(w) for w in A)
    print(*new_data)
