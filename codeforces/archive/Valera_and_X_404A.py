# Time: Jul/03/2022 21:32
# Title: A - Valera and X
# Submission ID: 162672928
# Language: Python


n = int(input())
a = []
for i in range(n):
    b = input()
    a.append(list(b))

def x():
    c = a[n//2][n//2]
    for i in range(n):
        if a[i][i] != c:
            return False
    for i in range(n):
        if a[i][n-i-1] != c:
            return False
    nc= a[0][1]
    if c == nc:
         return False
    count = n*n - 2*n + 1
    y = 0
    for i in a:
        y+= i.count(nc)
    return y == count

print("YES" if x() else 'NO')
