# Time: Jun/29/2022 07:32
# Title: A - Appleman and Toastman
# Submission ID: 162198202
# Language: Python


n = int(input())
x = [int(i) for i in input().split()]
s = 0
r = 2
x.sort()
for i in x:
    s += i * r
    r += 1
s -= x[-1]
print(s)
