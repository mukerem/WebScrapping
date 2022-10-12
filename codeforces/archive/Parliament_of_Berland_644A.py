# Time: Jun/29/2022 18:29
# Title: A - Parliament of Berland
# Submission ID: 162257946
# Language: Python


n,r,c = [int(i) for i in input().split()]
if n > r*c:
    print(-1)
    import sys
    sys.exit(0)
p = [[0 for i in range(c)] for j in range(r)] 
if c % 2:
    num = 1
    x = 0
    y = 0
    while num <= n:
        p[x][y] = num
        
        num += 1
        y += 1
        
        if y == c:
            y = 0
            x += 1
elif r % 2:
    num = 1
    x = 0
    y = 0
    while num <= n:
        p[x][y] = num
        num += 1
        x += 1
        if x == r:
            x = 0
            y += 1
else:
    num = 1
    x = 0
    y = 0
    while num <= n:
        p[x][y] = num
        num += 1
        y += 1
        if y == c-1:
            y = 0
            x += 1
        if x == r:
            break
    if num%2 == 0:
        for i in range(r):
            if num > n:
                break
            p[i][c-1] = num
            num += 1
    else:
        for i in range(r-1, -1, -1):
            if num > n:
                break
            p[i][c-1] = num
            num += 1
for row in p:
    print(*row)
        
            
