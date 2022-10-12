# Time: Jun/29/2022 21:37
# Title: A - Table
# Submission ID: 162273174
# Language: Python


r, c = [int(i) for i in input().split()]
x = []
for _ in range(r):
    a = [int(i) for i in input().split()]
    x.append(a)

def min_operation():
    def all_color():
        for i in x:
            for j in i:
                if j == 0:
                    return False
        return True

    if all_color():
        return 0
    if x[0][0] == 1 or x[0][c-1] == 1 or x[r-1][0] == 1 or x[r-1][c-1] == 1:
        return 1

    for i in range(r):
            if x[i][0] == 1 or x[i][c-1] == 1:
                return 2
    for i in range(c):
            if x[0][i] == 1 or x[r-1][i] == 1:
                return 2
    return 4
print(min_operation())
