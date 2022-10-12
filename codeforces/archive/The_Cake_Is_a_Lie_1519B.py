# Time: Jul/17/2022 09:09
# Title: B - The Cake Is a Lie
# Submission ID: 164577311
# Language: Python


t = int(input())
while t > 0:
    n, m, k = map(int, input().split())
    if k == n * m - 1:
        print('Yes')
    else:
        print('No')
    t -= 1
