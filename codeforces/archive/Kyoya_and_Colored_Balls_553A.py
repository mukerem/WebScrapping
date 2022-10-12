# Time: Jun/30/2022 20:11
# Title: A - Kyoya and Colored Balls
# Submission ID: 162365132
# Language: Python


from typing import List

def ways_to_draw_balls_from_bag(k:int, cs:List[int])->int:
    # the permutation take a long time for maximum number 1005, 
    # so minimize the range only for the largest number among the colors
    size = min(1005, sum(cs))
    mod = int(1e9) + 7
    per = [[0 for i in range(size)] for  j in range(size)]
    for i in range(size):
        per[i][0] = 1
        per[i][i] = 1
    for i in range(1, size):
        for j in range(1, i):
            per[i][j] = (per[i-1][j-1] + per[i-1][j]) % mod
    
    answer = 1
    total = 0
    for c in cs:
        total += c
        way = per[total - 1][c - 1]
        answer = (answer * way) % mod
    return answer
t = int(input())
a = []
for i in range(t):
    a.append(int(input()))
print(ways_to_draw_balls_from_bag(t,a))
