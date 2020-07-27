while True:
    try:
        a=str(input())
        v=0
        l,u,n=0,0,0
        for i in a:
            if i.isdigit():
                n+=1
            elif i.isupper():
                u+=1
            elif i.islower():
                l+=1
            if l!=0 and u!=0 and n!=0:
                v+=1
                l,u,n=0,0,0
            #print(i)
            #print(l,u,n)
            #print(v)
        print(v)
     
    except:
        break
