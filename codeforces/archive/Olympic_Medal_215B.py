# Time: Jul/20/2022 19:59
# Title: B - Olympic Medal
# Submission ID: 165035157
# Language: Python


from math import sqrt
f = lambda: list(map(int, input().split()))
r1 = max(f()[1:])
p1s = f()[1:]
p2 = min(f()[1:])
a, b = f()
print(str(sqrt(max(b * p1 * r1**2 / float(a * p2 + b * p1) for p1 in p1s))))
