# Time: Jul/16/2022 21:33
# Title: B - Sorted Adjacent Differences
# Submission ID: 164538383
# Language: Python


for _ in range(int(input())):
    n = int(input())
    ls = sorted(list(map(int, input().split())))
    mid = n // 2
    if n % 2 == 0:
        mid -= 1
    i = mid - 1
    turn = True
    j = mid + 1
    ar = []
    ar.append(ls[mid])
    while i >= 0 or j < n:
        if turn and j < n:
            ar.append(ls[j])
            j += 1
        elif not turn and i >= 0:
            ar.append(ls[i])
            i -= 1
        turn = not turn
    print(*ar)
