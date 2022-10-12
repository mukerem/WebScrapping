# Time: Jul/18/2022 22:58
# Title: B - New Year Permutation
# Submission ID: 164814184
# Language: Python


par=[0]*310
rank=[0]*310
def init_union_find(V):#initial state
    for i in range(V):
        par[i]=i
        rank[i]=0
def find(x):#where the root
    if par[x]==x:
        return x
    else:
        par[x]=find(par[x])
        return par[x]
def unite(x,y):#x and y unite
    x=find(x)
    y=find(y)
    if x==y:
        return
    if rank[x]<rank[y]:
        par[x]=y
    else:
        par[y]=x
        if(rank[x] == rank[y]): rank[x] += 1
def same(x,y):#x and y same root?
    return find(x)==find(y)

init_union_find(310)
edge=[0]*310
node=[0]*310
N=int(input())
p=list(map(int, input().split()))
uv=[]
for i in range(N):
    s=str(input())
    for j in range(N):
        if s[j]=='1':
            uv.append([i,j])
for u,v in uv:
    unite(u,v)
list=[0]*310
for i in range(len(p)):
    for j in range(i+1,len(p)):
        if p[i]>p[j] and find(i)==find(j):
            p[i],p[j]=p[j],p[i]
print (" ".join(map(str,p)))
