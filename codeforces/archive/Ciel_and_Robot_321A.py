# Time: Jun/27/2022 21:25
# Title: A - Ciel and Robot
# Submission ID: 161982712
# Language: Python


a,b = [int(i) for i in input().split()]
s = input()

x = 0
y = 0
m = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0)
}

for i in s:
    u,v = m[i]
    x += u
    y += v
def move(a, b):
    #print(a, b, x, y)
    if a == 0 and b == 0:
        return True
    if x == 0:
        if a != 0:
            return False
        k1 = 0
    else:
        if a == 0:
            return False
        elif a%x == 0:
            k1 = a//x
        else:
            return False
    #print(k1)
    if y == 0:
        if b != 0:
            return False
        k2 = 0
    else:
        if b == 0:
            return False
        elif b%y == 0:
            k2 = b//y
        else:
            return False
    if k1 < 0 or k2 < 0:
        return False
    if k1*k2 == 0 or k1 == k2:
        return True
    return False

dx = 0
dy = 0
for i in s:
    #print(a, b)
    res = move(a, b)
    if res:
        print('Yes')
        break
    u,v = m[i]
    a -= u
    b -= v
else:
    print('No')
    
