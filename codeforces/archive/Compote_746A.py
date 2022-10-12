# Time: Jun/29/2022 12:32
# Title: A - Compote
# Submission ID: 162224512
# Language: Python


a = int(input())
b = int(input())
c = int(input())
x = a
y = b/2
z = c/4
if min(x,y,z) == x:
    a,b,c = a, 2*a, 4*a
elif min(x,y,z) == y:
    w = b - b%2
    a,b,c = w//2, w, w*2
else:
    w = c - c%4
    a,b,c = w//4, w//2, w
print(a+b+c)
