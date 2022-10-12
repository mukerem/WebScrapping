# Time: Jun/29/2022 20:56
# Title: A - Sea Battle
# Submission ID: 162269956
# Language: Python


w1,h1,w2,h2 = [int(i) for i in input().split()]

if w1 == w2:
    ans = w1 + w2 + h1 + h1 + h2 + h2 + 4
else:
    ans = w1 + w1 + h1 + h1 + h2 + h2 + 4
print(ans)
