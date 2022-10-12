# Time: Jul/16/2022 21:02
# Title: B - Queue
# Submission ID: 164535456
# Language: Python


from typing import List

def walrus_displeasure(n: int, arr: List[int]) -> List[int]:
    result = [-1] * n
    arr = [(val, idx) for idx, val in enumerate(arr)]
    arr.sort()
    
    maxx = -1
    for val, idx in arr:
        if maxx < idx:
            result[idx] = -1
            maxx = idx
        else:
            result[idx] = maxx - idx - 1
    return result

n = int(input())
a = [int(i) for i in input().split()]
print(*walrus_displeasure(n, a))
