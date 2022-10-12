# Time: Jun/29/2022 11:37
# Title: A - Triangle
# Submission ID: 162219176
# Language: Python


from math import sqrt
x1,y1,x2,y2,x3,y3 = [int(i) for i in input().split()]

def is_right(x1,y1,x2,y2,x3,y3):
    if any([abs(i)>100 for i in (x1,y1,x2,y2,x3,y3)]):
        return False
    
    a = (x1-x2)**2 + (y1-y2)**2
    b = (x1-x3)**2 + (y1-y3)**2
    c = (x3-x2)**2 + (y3-y2)**2

    if any([abs(i)<=0 for i in (a,b,c)]):
        return False
    
    z = [a,b,c]
    z.sort()
    a,b,c = z
    if a + b == c:
        return True
    return False

def shift(x, y, d):
    x += d[0]
    y += d[1]
    return (x,y)

if is_right(x1,y1,x2,y2,x3,y3):
    print('RIGHT')
else:
    d = [(0,1),(0,-1),(1,0),(-1,0)]
    for i in d:
        u1,v1 = shift(x1, y1, i)
        u2,v2 = shift(x2, y2, i)
        u3,v3 = shift(x3, y3, i)
        if is_right(u1,v1,x2,y2,x3,y3) or\
           is_right(x1,y1,u2,v2,x3,y3) or\
           is_right(x1,y1,x2,y2,u3,v3):
            print('ALMOST')
            break
    else:
        print('NEITHER')
    
