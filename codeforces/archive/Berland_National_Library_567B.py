# Time: Aug/08/2022 16:39
# Title: B - Berland National Library
# Submission ID: 167521315
# Language: Python


from typing import List, Tuple

def possible_capacity(n: int, e: List[Tuple[str, str]]) -> int:
    id_number = []
    count = 0
    reader = 0
    
    for sign, id in e:
        if sign == '+':
            id_number.append(id)
            reader += 1
        else:
            if id in id_number:
                id_number.remove(id)
                reader -= 1
            else:
                count += 1
        count = max(count, reader)
                
    return count

n = int(input())
a = []
for i in range(n):
    b,c = input().split()
    a.append((b, c))
d = possible_capacity(n, a)
print(d)
