# Time: Jun/29/2022 23:21
# Title: A - Nauuo and Cards
# Submission ID: 162279330
# Language: Python


from typing import List
'''
def minimum_operations(n:int,A:List[int],B:List[int])->int:
    def rotate():
        dif = []
        for x in range(1, n+1):
            if x in B:
                position = B.index(x) + 1
                # x is the final position for a number x
                # position is the initial index(position) for a number x
                dif.append(position - x)
        if dif:
            return max(dif) + n + 1
        return n # if all numbers are at Nuuno's hand
    
    if 1 in B:
        idx = B.index(1)
        k = n - idx
        
        if B[-k:] == list(range(1, k+1)):
            dif = []
            for x in range(k+1, n+1):
                
                if x in B:
                    position = B.index(x) + 1
                    # x is the final position for a number x
                    # position is the initial index(position) for a number x
                    if position >= x-k:
                        dif.append(position - x)
            if dif:
                return max(0, max(dif)) + n + 1
            return idx
        else:
            return rotate()
    else:
        return rotate()
'''

def minimum_operations(n:int,A:List[int],B:List[int])->int:
    z = [0 for i in range(n + 1)]
    for idx, i in enumerate(B):
        z[i] = idx + 1
        
    def rotate():
        maxx = -1
        for x in range(1, n+1):
            maxx = max(maxx, z[x] - x)
        return maxx + 1 + n
    
    if 1 in B:
        idx = z[1]
        k = n - idx + 1
        if B[-k:] == list(range(1, k+1)):
            
            maxx = -1
            for x in range(k+1, n+1):
                if x-k-1 < z[x]:
                    break
            else:
                return idx-1
            return rotate()
        else:
            return rotate()
    else:
        return rotate()
            
n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
print(minimum_operations(n,a,b))
