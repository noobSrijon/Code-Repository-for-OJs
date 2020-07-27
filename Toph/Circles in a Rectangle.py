for _ in range(int(input())):
    r=float(input())
    r_area=8*(r**2)
    ans=r_area-((3.1416*(r**2)+(3.1416*(r**2))))
    print("Case {}: {}".format(_+1,"%.2f" %ans))
