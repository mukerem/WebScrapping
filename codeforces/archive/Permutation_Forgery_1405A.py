# Time: Jun/27/2022 14:33
# Title: A - Permutation Forgery
# Submission ID: 161943567
# Language: Python


for _ in range(int(input())):
    n = int(input())
    x = [int(i) for i in input().split()]
    print(*x[::-1])
