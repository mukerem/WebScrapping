# Time: Jul/15/2022 19:06
# Title: B - Bear and Forgotten Tree 3
# Submission ID: 164340623
# Language: Python


n, d, h = list(map(int, input().split()))
if h < (d + 1) // 2 or (h == d == 1 and n > 2):
    print(-1)
    exit()

i = 1
while i <= h:
    print(i, i + 1)
    i += 1
if i <= d:
    print(1, h + 2)
    i = h + 2
while i <= d:
    print(i, i + 1)
    i += 1
i += 1
while i <= n:
    if h == d:
        print(2, i)
    else:
        print(1, i)
    i += 1
