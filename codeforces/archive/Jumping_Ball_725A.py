# Time: Jul/04/2022 21:49
# Title: A - Jumping Ball
# Submission ID: 162819931
# Language: Python


n = int(input())
a = input()
x = 0
for i in a:
    if i == '>':
        break
    x += 1
for  i in a[::-1]:
    if i == '<':
        break
    x += 1
print(x)
