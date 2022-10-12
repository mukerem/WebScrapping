# Time: Aug/11/2022 11:45
# Title: B - Longtail Hedgehog
# Submission ID: 167845457
# Language: Python


from typing import List, Tuple

def max_beauty(n: int, m: int, points: List[Tuple[int, int]]) -> int:
    maxN = 100005
    dp = [0] * maxN
    edge = [[] for i in range(maxN)]
    
    for u, v in points:
        edge[u].append(v)
        edge[v].append(u)
        
    ans = -1;
    for v in range(1, n+1):
        dp[v] = 1
        for u in edge[v]:
            if u < v:
                dp[v] = max(dp[v], dp[u] + 1)
        ans = max(ans, dp[v] * len(edge[v]))
    return ans

n,m = map(int, input().split())
a = []
for i in range(m):
    b,c = map(int, input().split())
    a.append((b, c))
print(max_beauty(n, m, a))
