# Time: Jun/29/2022 16:05
# Title: A - Snacktower
# Submission ID: 162244100
# Language: Python


n = int(input())
x = [int(i) for i in input().split()]
e = [False] * (n + 1)
target = n
for i in x:
    e[i] = True
    if i == target:
        while e[target]:
            print(target, end= ' ')
            target -= 1
        else:
            print()
    else:
        print()
