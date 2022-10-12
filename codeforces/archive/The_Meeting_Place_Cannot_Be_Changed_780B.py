# Time: Jul/16/2022 15:24
# Title: B - The Meeting Place Cannot Be Changed
# Submission ID: 164443054
# Language: Python


def solve(t,x,v):
    l=[x[i]-v[i]*t for i in range(len(x))]
    r=[x[i]+v[i]*t for i in range(len(x))]
    return 1 if max(l)<=min(r) else 0

n=int(input())
x=list(map(int,input().split()))
v=list(map(int,input().split()))
l=0
h=10**9
cnt=0
while l<h and cnt<100:
    mid=l+(h-l)/2
    cnt+=1
    if solve(mid,x,v):
        h=mid
    else:
        l=mid
print(l)
