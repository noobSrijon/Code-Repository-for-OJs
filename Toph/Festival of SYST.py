for _ in range(int(input())):
    A=str(input())
    A=list(A)
    if ",EEE" in A or ".EEE" in A or "EEE," in A or "EEE." or "EEE" in A or ",CSE" in A or ".CSE" in A or "CSE," in A or "CSE." or "CSE" in A or ",SWE" in A or ".SWE" in A or "SWE," in A or "SWE." or "SWE" in A :
        print("SUST Tech Fest")
    elif ",CSE" in A or ".CSE" in A or "CSE," in A or "CSE." or "CSE" in A:
        print("SUST CSE Carnival")
    else:
        print("Festival of SUST")
