# Time: Jul/03/2022 17:37
# Title: A - GukiZ and Contest
# Submission ID: 162654074
# Language: Python


n = int(input())
x = [int(i) for i in input().split()]

y = x[:]
y.sort(reverse=True)

a = []
for i in x:
    idx = y.index(i) + 1
    a.append(idx)
print(*a)
