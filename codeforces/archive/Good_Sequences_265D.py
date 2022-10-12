# Time: Jul/15/2022 23:16
# Title: D - Good Sequences
# Submission ID: 164365955
# Language: Python


from math import *
N=100002
dp=[0]*N
n=int(input())
a=[int(x) for x in input().split(' ')]
minPrime=[0]*(N+1)
for i in range(2,N):
    if minPrime[i]==0:
        minPrime[i]=i
        max_j=N//i
        for j in range(i,max_j+1):
            if minPrime[i*j]==0:
                minPrime[i*j]=i
res=0
for c in a:
    tmp=c
    t_ans=0
    while tmp>1:
        t_ans = max(t_ans, dp[minPrime[tmp]]);
        tmp //= minPrime[tmp];
    t_ans+=1
    res=max(res, t_ans);
    tmp=c;
    while tmp>1:
        dp[minPrime[tmp]] = max(t_ans, dp[minPrime[tmp]]);
        tmp //= minPrime[tmp];
print(res)
