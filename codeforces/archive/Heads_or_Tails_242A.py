# Time: Jul/03/2022 16:45
# Title: A - Heads or Tails
# Submission ID: 162649152
# Language: Python


x,y,a,b = [int(i) for i in input().split()]
ans = []
for i in range(a,x+1):
    for j in range(b, y+1):
        if i>j:
            ans.append((i,j))
print(len(ans))
for i in ans:
    print(*i)
