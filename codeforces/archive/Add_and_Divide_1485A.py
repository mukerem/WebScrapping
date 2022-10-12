# Time: Jul/05/2022 17:51
# Title: A - Add and Divide
# Submission ID: 162907093
# Language: Python


from typing import List

def min_operations_to_zero(t:int, lst:List[int])->int:
    def to_zero(a,b):
        c = 0
        while a:
            a = a//b
            c += 1
        return c
    ans = []
    for a,b in lst:
        best = 1000000
        if b>1:
            best = to_zero(a,b)
        for i in range(1, 30):
            k = to_zero(a,b+i) + i
            best = min(best, k)
        ans.append(best)
    return ans
t = int(input())
x = []
for i in range(t):
    a,b = [int(_) for _ in input().split()]
    x.append((a,b))
y = min_operations_to_zero(t, x)
for i in y:
    print(i)
