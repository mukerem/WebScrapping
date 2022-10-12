# Time: Jul/03/2022 10:34
# Title: A - Circle Line
# Submission ID: 162615495
# Language: Python


n = int(input())
x = [int(i) for i in input().split()]
s,t = [int(i) for i in input().split()]
s-=1
t-=1
x += x[:-1]
if s>t:
    s,t=t,s
a = sum(x[s:t])
b = sum(x[t:n+s])
print(min(a,b))
