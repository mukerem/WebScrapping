# Time: Jun/30/2022 14:05
# Title: A - Red and Blue Beans
# Submission ID: 162329351
# Language: Python


from typing import List, Tuple

def can_distribute_all_beans(t: int, test_cases: List[Tuple[int, int ,int]]) -> List[str]:
    answer = []
    for r,b,d in test_cases:
        x = min(r,b)
        y = max(r,b)
        if x * (1+d) >= y:
            answer.append('YES')
        else:
            answer.append('NO')
    return answer
t = int(input())
a = []
for _ in range(t):
    r,b,d = [int(i) for i in input().split()]
    a.append((r,b,d))
b = can_distribute_all_beans(t, a)
for i in b:
    print(i)
