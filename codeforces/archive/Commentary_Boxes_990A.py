# Time: Jul/05/2022 12:32
# Title: A - Commentary Boxes
# Submission ID: 162876445
# Language: Python


n,m,a,b = [int(i) for i in input().split()]
x = n//m
y = x + 1

u = n - x*m
v = m*y - n
w = u*b
z = v*a
print(min(w, z))
