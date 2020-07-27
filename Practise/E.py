date1=str(input())
date2=str(input())
d1=date1.split("-")
d2=date2.split("-")
if d1[0]>d2[0]:
    print(int(d1[0])-int(d2[0]))
elif d1[0]<d2[0]:
    print(int(d2[0])-int(d1[0])) 
