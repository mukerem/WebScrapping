# Time: Aug/05/2022 17:10
# Title: B - Embassy Queue
# Submission ID: 167113448
# Language: Python


from collections import deque
from typing import List

def maximum_time_spend(k1: int, k2: int, k3: int, t1: int, t2: int, t3: int,
                       n: int, oq: List[int]) -> int:

    k = [k1, k2, k3]
    t = [t1, t2, t3]
    c = [[0] * n for i in range(3)]
    s = 0
    for i in range(n):
        x = oq[i]
        y = x

        for j in range(3):
            r = i%k[j]
            c[j][r] = max(c[j][r], y) + t[j]
            y = c[j][r]	

        s=max(s,y-x)
	
    return s
    

k = list(map(int, input().split()))
t = list(map(int, input().split()))
n = int(input())
a = list(map(int, input().split()))
b = maximum_time_spend(*k, *t, n, a)
print(b)
