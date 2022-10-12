# Time: Aug/08/2022 22:30
# Title: B - Prison Transfer
# Submission ID: 167556359
# Language: Python


from typing import List

def no_of_ways_to_choose_prisoners(n:int, t:int, c:int, p:List[int])->int:
    v = [-1]
    for i in range(n):
        if p[i] > t:
            v.append(i)
    
    v.append(n)
    ans = 0
    for i in range(1, len(v)):
        diff = v[i] - v[i-1] - 1
        ans += max( diff - c + 1 , 0 )
    return ans

n,t,c = map(int, input().split())
a = list(map(int, input().split()))

b = no_of_ways_to_choose_prisoners(n, t, c, a)
print(b)
