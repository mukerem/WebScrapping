# Time: Jul/16/2022 19:40
# Title: B - Balanced Substring
# Submission ID: 164527309
# Language: Python


inp=lambda:map(int,input().split())
n=int(input())
s=input()

a0=[0]*(10**5+1)
a1=[0]*(10**5+1)

if(s[0]=='0'):
   a0[0]=1
else:
   a1[0]=1


for i in range(1,n):
    if(s[i]=='0'):
        a0[i]=a0[i-1]+1
        a1[i]=a1[i-1]
    else:
        a0[i]=a0[i-1]
        a1[i]=a1[i-1]+1


lab=[-2]*(2*10**5+1)
m=[-1]*(2*10**5+1)
lab[10**5]=-1

for i in range(n):
    if lab[a0[i]-a1[i]+10**5]>=-1:
       m[a0[i]-a1[i]+10**5]=max(m[a0[i]-a1[i]+10**5], i-lab[a0[i]-a1[i]+10**5])
    else:
       lab[a0[i]-a1[i]+10**5]=i 

t=-1;
for i in range(2*10**5+1):
    t=max(t,m[i])

print(max(t,0))
