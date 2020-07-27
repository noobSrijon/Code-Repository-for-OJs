"""import math
A=int(input())
B=int(input())
Areafull=(0.5*A*B)
MC=(((A**2)+(B**2))**0.5)/2
MB=Areafull/(((A**2)+(B**2))**0.5)
Angle=math.acos(math.radians(((B**2)+(MB**2)-(MC**2))/(2*B*MB)))
print(math.degrees(Angle))
"""
import math
AB = float(input())
BC = float(input())

print(str(int(round(math.degrees(math.atan(AB/BC)))))+'°')
