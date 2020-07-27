import math
hour,minute=map(float,input().split())
angle_1 = (hour*5.0) + (minute/12.0)
angle_1 *= 6.00
angle_2 = (minute*6.00)
cell = math.fabs(angle_1 - angle_2)
cell = min(cell, (360-cell))
print("%.7f"%cell);
