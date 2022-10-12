# Time: Jul/04/2022 19:50
# Title: A - Eating Soup
# Submission ID: 162809089
# Language: Python


n,m = [int(i) for i in input().split()]
if m == 0 or m == 1:
    print(1)
else:
    print(min(m, n-m))
