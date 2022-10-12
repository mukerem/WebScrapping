# Time: Aug/04/2022 17:43
# Title: A - 2-3 Moves
# Submission ID: 166940211
# Language: Python


for _ in range(int(input())):
    n = int(input())
    k = n//3
    if n ==4 or n == 1:
        print(2)
    elif n%3 == 0:
        print(k)
    elif n%3 == 1:
        print(k+1)
    else:
        print(k+1)
