# Time: Aug/08/2022 15:37
# Title: B1 - The Doctor Meets Vader (Easy)
# Submission ID: 167514164
# Language: Python


from bisect import bisect_right
from typing import List, Tuple

def maximum_gold_each_spaceship_can_steal(s: int, b: int, a: List[int], bases: List[Tuple[int, int]]) -> List[int]:
    bases = sorted(bases)
    cummulative_summation = []
    total = 0
    for power, gold in bases:
        total += gold
        cummulative_summation.append(total)
    
    bases_power = [power for power, gold in bases]
    max_gold = []
    for power in a:
        r = bisect_right(bases_power, power)
        if r == 0:
            max_gold.append(0)
            continue
        r -= 1
        gold = cummulative_summation[r]
        max_gold.append(gold)
    return max_gold

s,b = map(int, input().split())
a = [int(i) for i in input().split()]
bases = []
for i in range(b):
    bases.append([int(j) for j in input().split()])
    
c = maximum_gold_each_spaceship_can_steal(s, b, a, bases)
print(*c)
