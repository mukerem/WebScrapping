# Time: Jun/30/2022 22:17
# Title: A - Rectangle Puzzle
# Submission ID: 162374759
# Language: Python


'''
from math import sin, cos, tan, pi
w,h,alp = [int(i) for i in input().split()]
alp = alp * pi/180
x = sin(alp)
y = 1 + cos(alp)

f = (y*h -x*w) / (y*y - x*x)
c = (w - x*f) / y
a = c * cos(alp)
b = c * sin(alp)
d = f * cos(alp)
e = f * sin(alp)

area = w * h - a*b - d*e
print(area)
'''


from math import sin, cos,atan,tan, pi, sin
def common_area_rotated_triangles(w: int, h: int, a: int) -> float:
    if h>w: h,w = w,h
    if a == 0 or a== 180:
        return w*h
    if a>90:
        a = 180-a
    b = 2*atan(h/w)
    b = b * 180 / pi
    #print(b, a)
    if 0 <= a <= b:
        
        a = a * pi/180
        x = sin(a)
        y = 1 + cos(a)

        f = (y*h -x*w) / (y*y - x*x)
        c = (w - x*f) / y
        aa = c * cos(a)
        b = c * sin(a)
        d = f * cos(a)
        e = f * sin(a)
        area = w * h - aa*b - d*e
        return area
    else:
        base = h / sin(a * pi/180)
        area = base * h
        return area

w,h,a = [int(i) for i in input().split()]
print(common_area_rotated_triangles(w,h,a))
