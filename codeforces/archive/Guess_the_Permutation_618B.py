# Time: Jul/14/2022 20:33
# Title: B - Guess the Permutation
# Submission ID: 164176244
# Language: Python


# from pprint import pprint

n = int(input())
a = []
for i in range(n):
    row = [int(k) for k in input().split()]
    a.append(row)

result = [0] * n
for k in range(1, n):
    # print('k=', k)
    for i in range(n):
        countK = 0
        countNonK = 0
        for j in range(n):
            if a[i][j] == k:
                countK += 1
            elif a[i][j] != 0:
                countNonK += 1
        # print('@', countK, countNonK)
        if countK > 0 and countNonK == 0:
            # print('j', j)
            result[i] = k
            for j in range(n):
                a[i][j] = 0
                a[j][i] = 0
            continue

        countK = 0
        countNonK = 0
        for j in range(n):
            if a[j][i] == k:
                countK += 1
            elif a[j][i] != 0:
                countNonK += 1
        if countK > 0 and countNonK == 0:
            # print('j#', j)
            result[i] = k
            for j in range(n):
                a[j][i] = 0
                a[i][j] = 0
    # pprint(a)
result[result.index(0)] = n

print(' '.join(str(i) for i in result))
