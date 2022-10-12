# Time: Jun/28/2022 15:52
# Title: C - Lorenzo Von Matterhorn
# Submission ID: 162046271
# Language: Python


path = {}
def set_cost(u, v, w):
    edge = []
    while v != u:
        if v<u:
            u,v = v,u
        p = (v//2, v)
        if p in path: path[p] += w
        else: path[p] = w
        v = v//2
    #print(path)
def get_cost(u, v):
    edge = []
    cost = 0
    while v != u:
        if v<u:
            u,v = v,u
        p = (v//2, v)
        if p in path: cost += path[p]
        v = v//2
    return cost

for _ in range(int(input())):
    x = [int(i) for i in input().split()]
    if x[0] == 2:
        u,v = x[1:]
        print(get_cost(u, v))
    else:
        u,v,w = x[1:]
        set_cost(u, v, w)
