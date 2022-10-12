# Time: Aug/08/2022 20:32
# Title: B - Average Superhero Gang Power
# Submission ID: 167545222
# Language: Python


from typing import List

def maximum_final_average_power(n: int, k: int, m: int, heroes: List[int]) -> float:
    heroes = sorted(heroes)
    power_sum = [0]
    total = 0
    for power in heroes:
        total += power
        power_sum.append(total)
    
    average = 0
    for i in range(n):
        if i>m:
            break
        summation = total - power_sum[i] + min(m-i, k * (n-i))
        ave = float(summation) / (n-i)
        average = max(average, ave)
    return average

n, k, m = map(int, input().split())
b = [int(j) for j in input().split()]

a = maximum_final_average_power(n, k, m, b)
print(a)
