# Time: Aug/05/2022 15:41
# Title: B - Fox And Two Dots
# Submission ID: 167102479
# Language: Python


from typing import List

def exists_a_cycle_on_the_field(n: int, m: int, colors: List[str]) -> str:
    graph = [[] for i in range(n*m)]
    for i in range(n):
        for j in range(m):
            u = i * m + j
            u_color = colors[i][j]
            
            if i+1 < n and u_color == colors[i+1][j]:
                v = (i+1) * m + j
                graph[u].append(v)
                graph[v].append(u)
            
            if j+1 < m and u_color == colors[i][j+1]:
                w = i * m + j + 1
                graph[u].append(w)
                graph[w].append(u)
    
    def isCyclicUtil(v, visited, parent):
        visited[v] = True
        for i in graph[v]:
            if visited[i] == False:
                if isCyclicUtil(i, visited, v):
                    return True
            elif parent != i:
                return True
        return False

    def isCyclic(size):
        visited = [False] * size
        for i in range(size):
            if visited[i] == False:
                if isCyclicUtil(i, visited, -1) == True:
                    return True

        return False
    size = n*m
    if isCyclic(size) == True:
        return 'Yes'
    return 'No'

n,m = map(int, input().split())
a = []
for i in range(n):
    a.append(input())
print(exists_a_cycle_on_the_field(n, m, a))
