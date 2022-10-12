# Time: Jun/30/2022 11:43
# Title: A - Sereja and Coat Rack
# Submission ID: 162317476
# Language: Python


from typing import List

def calculate_profit(racks: int, fine: int, cost: List[int], guests: int) -> int:
    cost.sort()
    
    if guests > racks:
        pay = (guests -racks) * fine
        get = sum(cost) # All of the hooks are used by the guests
        profit = get - pay
    else:
        get = sum(cost[:guests]) # Only m hooks are used by the guests
        profit  = get
    return profit
        
n,d = [int(i) for i in input().split()]
x = [int(i) for i in input().split()]
m = int(input())

print(calculate_profit(n, d , x, m))
