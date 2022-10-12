# Time: Jun/27/2022 11:40
# Title: A - Puzzle Pieces
# Submission ID: 161928282
# Language: Python


for _ in range(int(input())):
    a,b = [int(i) for i in input().split()]
    t = a*b
    per = 2 * (a + b)
    if t + per >= 3*t:
        print('YES')
    else:
        print('NO')
    
