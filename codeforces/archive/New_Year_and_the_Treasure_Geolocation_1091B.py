# Time: Aug/05/2022 19:40
# Title: B - New Year and the Treasure Geolocation
# Submission ID: 167132497
# Language: Python


from typing import List, Tuple

def coordinates_of_the_treasure(n: int, coordinates: List[Tuple[int, int]], directions: List[Tuple[int, int]]) -> Tuple[int, int] :    
    
    min_obelisk = min(coordinates)
    max_clue = max(directions)
    
    return min_obelisk[0] + max_clue[0], min_obelisk[1] + max_clue[1]
        
n  = int(input())
a = []
b = []
for i in range(n):
    a.append(tuple(map(int, input().split())))

for i in range(n):
    b.append(tuple(map(int, input().split())))

c = coordinates_of_the_treasure(n, a, b)
print(*c)
