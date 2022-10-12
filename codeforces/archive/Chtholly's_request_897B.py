# Time: Jul/15/2022 21:54
# Title: B - Chtholly's request
# Submission ID: 164359776
# Language: Python


import itertools as it
k, p = [int(elem) for elem in input().split()]

def build_palindroms(digits):
    global k
    global val
    n = digits // 2
    values = [10 ** (digits - 1 - i) + 10 ** i for i in range(n)]
    for comb in it.product(range(1, 10), *[range(0, 10) for i in range(n - 1)]):
        if not k:
            return False
        for j, dig in enumerate(comb):
            val += dig * values[j]
        k -= 1
    return True
val = 0
j = 2
while build_palindroms(j):
    j += 2

print(val % p)
