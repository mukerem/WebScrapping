# Time: Aug/09/2022 08:03
# Title: B - Finding Team Member
# Submission ID: 167587669
# Language: Python


from typing import List

def get_contestant_teammates(n: int, values: List[List[int]]) -> List[int]:
    strength = []
    pair = [0] * (2*n + 1)
    for i in range(2*n-1):
        for j in range(i+1):
            strength.append((values[i][j], i + 2, j+1))
    
    strength.sort(reverse=True)
    for s, i, j in strength:
        if pair[i] == 0 and pair[j] == 0:
            pair[i] = j
            pair[j] = i
            
    return pair[1:]

n = int(input())
a = []
for i in range(2*n-1):
    b = [int(j) for j in input().split()]
    a.append(b)
b  = get_contestant_teammates(n, a)
print(*b)
