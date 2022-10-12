# Time: Aug/08/2022 21:23
# Title: B - Multiplication Table
# Submission ID: 167550406
# Language: Python


from math import sqrt
from typing import List

def restore_table(n: int, M: List[List[int]]) -> List[int]:
    ans = [0] * n
    for i in range(n):
        if i == 0:
            a, b = 1, 2
        elif i == n-1:
            a, b = n-3, n-2
        else:
            a, b = i-1, i+1
        
        ans[i] = int(sqrt(M[i][a] * M[i][b] // M[a][b]))
    return ans

n = int(input())
c = []
for i in range(n):
    b = [int(j) for j in input().split()]
    c.append(b)
a = restore_table(n, c)
print(*a)
