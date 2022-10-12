# Time: Jun/28/2022 19:45
# Title: A - Pineapple Incident
# Submission ID: 162152116
# Language: Python


t,s,x = [int(i) for i in input().split()]
def will_pineapple_bark(t:int, s:int, x:int)->str:
    if t == x: # the first bark time is t.
        return 'YES'
    k1 = (x - t) / s
    k2 = (x - t - 1) / s
    if k1 > 0 and k1 == int(k1):
        return 'YES'
    if k2 > 0 and k2 == int(k2):
        return 'YES'
    return 'NO'

print(will_pineapple_bark(t,s,x))
