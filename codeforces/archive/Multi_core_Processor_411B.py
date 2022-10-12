# Time: Aug/11/2022 21:03
# Title: B - Multi-core Processor
# Submission ID: 167901120
# Language: Python


from typing import List

def deadlock_situation(n: int, m: int, k: int, L: List[List[int]]) -> List[int]:
    blockedCell = [False] * (k+1)
    blockedCore = [0] * n
    for i in range(m):
        cells = {}
        for j in range(n):
            if blockedCore[j] != 0:
                continue
            cell = L[j][i]
            if cell == 0:
                continue
            if blockedCell[cell] == True:
                blockedCore[j] = i + 1
            elif cell in cells:
                #blockedCell[cell] = True
                cells[cell].append(j)
            else:
                cells[cell] = [j]
        for cell in cells:
            cores = cells[cell]
            if len(cores) > 1:
                blockedCell[cell] = True
                for core in cores:
                    blockedCore[core] = i + 1
    return blockedCore

n, m, k = map(int, input().split())
a = []
for i in range(n):
    b = [int(j) for j in input().split()]
    a.append(b)

c = deadlock_situation(n, m, k, a)
for i in c:
    print(i)
