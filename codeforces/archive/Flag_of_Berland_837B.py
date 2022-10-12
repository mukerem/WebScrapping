# Time: Aug/11/2022 08:50
# Title: B - Flag of Berland
# Submission ID: 167830875
# Language: Python


from typing import List

def flag_of_Berland(n: int, m: int, f: List[str]) -> str:
    # check horizontal strip
    def horizontal_flag():
        if n%3 != 0:
            return 'NO'
        k = n // 3
        first = f[0][0]
        second = f[k][0]
        third = f[2*k][0]
        if first == second or first == third or second == third:
            return 'NO'
        for i in range(k):
            for j in range(m):
                if f[i][j] != first:
                    return 'NO'

        for i in range(k, 2*k):
            for j in range(m):
                if f[i][j] != second:
                    return 'NO'

        for i in range(2*k, n):
            for j in range(m):
                if f[i][j] != third:
                    return 'NO'
                
        return 'YES'
    
    def vertical_flag():
        if m%3 != 0:
            return 'NO'
        k = m // 3
        first = f[0][0]
        second = f[0][k]
        third = f[0][2*k]
        if first == second or first == third or second == third:
            return 'NO'
        for i in range(n):
            for j in range(k):
                if f[i][j] != first:
                    return 'NO'

        for i in range(n):
            for j in range(k, 2*k):
                if f[i][j] != second:
                    return 'NO'

        for i in range(n):
            for j in range(2*k, m):
                if f[i][j] != third:
                    return 'NO'

        return 'YES'
    
    if horizontal_flag() == 'YES':
        return 'YES'
    return vertical_flag()

n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(input())
print(flag_of_Berland(n, m, a))
