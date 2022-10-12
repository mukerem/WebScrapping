# Time: Aug/05/2022 14:53
# Title: B - Orac and Models
# Submission ID: 167097184
# Language: Python


from math import sqrt
from typing import List, Tuple

def maximum_number_of_models(t: int, queries: List[Tuple[int, List[int]]]) -> List[int]:
    def divisors(n: int) -> List[int]:
        if n == 1:
            return []
        k = int(sqrt(n))
        div = [1]
        for i in range(2, k+1):
            if n%i == 0:
                div.append(i)
                div.append(n//i)
        if k*k == n:
            div.remove(k)
        return div
    
    answer = []
    for n, arr in queries:
        dp = [1] * (n+1)
        dp[1] = 1
        for i in range(2, n+1):
            div = divisors(i)
            for d in div:
                if arr[d-1] < arr[i-1]:
                    dp[i] = max(dp[i], dp[d] + 1)
        answer.append(max(dp[1:]))
    return answer
b = []
t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    b.append((n, a))
c = maximum_number_of_models(t, b)
for i in c:
    print(i)
    
