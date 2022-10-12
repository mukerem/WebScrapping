# Time: Jul/04/2022 18:44
# Title: A - Vasya and Socks
# Submission ID: 162793443
# Language: Python


n,m = [int(i) for i in input().split()]
t = n
while t>=m:
    z = t//m
    r = t%m
    n += z
    t = z + r
print(n)
