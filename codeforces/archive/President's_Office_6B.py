# Time: Aug/08/2022 14:49
# Title: B - President's Office
# Submission ID: 167508695
# Language: Python


from typing import List

def amount_of_President_deputies(n: int, m: int, c: str, desc: List[str]):
    x = []
    y = []
    for i in range(n):
        for j in range(m):
            if desc[i][j] == c:
                x.append(i)
                y.append(j)
    x1 = min(x)
    y1 = min(y)
    x2 = max(x)
    y2 = max(y)
    
    w = y2-y1+1
    h = x2-x1+1
    #print(x,y,x2,y2,x1,h)
    s = set()
    if y1 > 0:
        for i in range(x1, x1+h):
            if desc[i][y1-1] != '.':
                s.add(desc[i][y1-1])
    if y2 < m-1:
        for i in range(x1, x1+h):
            if desc[i][y2+1] != '.':
                s.add(desc[i][y2+1])
    if x1 > 0:
        for i in range(y1, y1+w):
            if desc[x1-1][i] != '.':
                s.add(desc[x1-1][i])
    if x2 < n-1:
        for i in range(y1, y1+w):
            if desc[x2+1][i] != '.':
                s.add(desc[x2+1][i])
    return len(s)
n,m,c = input().split()
n = int(n)
m = int(m)
a = []
for i in range(n):
    a.append(input())
b = amount_of_President_deputies(n,m,c,a)
print(b)
