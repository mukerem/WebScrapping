# Time: Aug/11/2022 12:25
# Title: B - Kyoya and Permutation
# Submission ID: 167849408
# Language: Python


from typing import List

def find_kth_permutation(n:int, k:int)->List[int]:
    fib = [0] * (n+1)
    fib[0] = fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    
    idx = 0
    res = [0] * n
    while idx < n:
        if k <= fib[n-idx-1]:
            res[idx] = idx + 1
            idx += 1
        else:
            k -= fib[n-idx-1]
            res[idx] = idx + 2
            res[idx+1] = idx + 1
            idx += 2
    return res    
n, k = map(int, input().split())
r = find_kth_permutation(n, k)
print(*r)
