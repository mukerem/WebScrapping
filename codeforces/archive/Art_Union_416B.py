# Time: Jul/13/2022 19:01
# Title: B - Art Union
# Submission ID: 164054200
# Language: Python


import sys
from typing import List, Tuple

def picture_painiting(m: int, n: int, arr: List[Tuple[int]]) -> List[int]:
    
    times = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            times[i][j] = int(arr[i-1][j-1])
    for i in range(1, m+1):
        for j in range(1, n+1):
            times[i][j] += max(times[i-1][j], times[i][j-1])

    ans = [ x[-1] for x in times[1:]]
    return ans
m,n = [int(i) for i in input().split()]
a = []
for _ in range(m):
    b = [int(i) for i in input().split()]
    a.append(b)
y = picture_painiting(m,n,a)
print(*y)
