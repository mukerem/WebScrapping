# Time: Aug/08/2022 18:37
# Title: B - Shower Line
# Submission ID: 167533150
# Language: Python


from itertools import permutations
from typing import List

def initial_order_for_maximum_happiness(mat: List[List[int]]) -> int:
    def calculate_happiness(student: List[int]) -> int:
        hap = 0
        n  = 5
        while student:
            pair = [(student[i], student[i+1]) for i in range(0, n-1, 2)]
            for i, j in pair:
                hap += mat[i][j]
                hap += mat[j][i]
            n -= 1
            student = student[1:]
        return hap
    num = [0, 1, 2, 3, 4]
    possible = list(permutations(num))
    happiness = 0
    for order in possible:
        hap = calculate_happiness(order)
        happiness = max(happiness, hap)
    return happiness

a = []
for i in range(5):
    b = [int(j) for j in input().split()]
    a.append(b)
d = initial_order_for_maximum_happiness(a)
print(d)
