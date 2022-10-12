# Time: Jun/30/2022 11:21
# Title: A - String Similarity
# Submission ID: 162315436
# Language: Python


from typing import List, Tuple

def binary_strings(t: int, strings: List[Tuple[str]]) -> List[str]:
    answer = []
    for n, s in strings:
        w = ''
        for i in range(1, 2*n + 1, 2):
            w += s[i-1]
        answer.append(w)
    return answer
            
a = []
t = int(input())
for i in range(t):
    n = int(input())
    a.append((n, input()))
b = binary_strings(t, a)
for i in b:
    print(i)
