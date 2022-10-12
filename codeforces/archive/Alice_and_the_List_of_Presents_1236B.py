# Time: Jul/19/2022 09:40
# Title: B - Alice and the List of Presents
# Submission ID: 164855036
# Language: Python


from sys import stdin, stdout
input = stdin.readline
mod=10**9+7
t = 1
for _ in range(t):
    n,m=map(int,input().split())
    print(pow((pow(2,m,mod)-1),n,mod))
