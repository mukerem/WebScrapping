# Time: Jul/05/2022 18:29
# Title: C - Drazil and Factorial
# Submission ID: 162910816
# Language: Python


x = input()
n = input()

d = {
    '4': ['3','2','2'],
    '6': ['5','3'],
    '8': ['7','2','2','2'],
    '9': ['7','2','3','3'] 
    }

ans = []
for i in n:
    if i == '1' or i == '0':
        continue
    if i in d:
        ans += d[i]
    else:
        ans.append(i)

ans.sort()
ans.reverse()
k = ''.join(ans)
print(k)
