# Time: Aug/11/2022 10:11
# Title: B - M-arrays
# Submission ID: 167837285
# Language: Python


from typing import List, Tuple

def smallest_m_divisible(t: int, testcases: List[Tuple[int, int, List[int]]]) -> List[int]:
    answer = []
    for n, m, arr in testcases:
        mod = {}
        for x in arr:
            r = x % m
            if r in mod:
                mod[r] += 1
            else:
                mod[r] = 1
        ct = 0
        if 0 in mod:
            ct += 1
            mod.pop(0)
        for x in mod:
            y = m - x
            if x == y:
                ct += 1
                continue
            if mod[x] != 0:
                a = mod[x]
                if y in mod:
                    b = mod[y]
                    ct += 1 + max(0, abs(a - b) - 1)
                    mod[y] = 0
                else:
                    ct += a
            mod[x] = 0
        answer.append(ct)
    return answer

t = int(input())
a = []
for i in range(t):
    n, m = map(int, input().split())
    b = [int(_) for _ in input().split()]
    a.append((n, m, b))
c = smallest_m_divisible(t, a)
for i in c:
    print(i)
