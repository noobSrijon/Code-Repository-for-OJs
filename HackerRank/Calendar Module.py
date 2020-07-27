import calendar
x=["SUNDAY","MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY"]
calendar.setfirstweekday(calendar.SUNDAY)
A=str(input())
A=A.split(" ")
A=calendar.weekday(int(A[2]), int(A[1]), int(A[0]))
print(x[A-1])
