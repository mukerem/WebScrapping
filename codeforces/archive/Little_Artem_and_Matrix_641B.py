# Time: Jul/18/2022 09:45
# Title: B - Little Artem and Matrix
# Submission ID: 164686048
# Language: Python


from collections import *
def main():
    n,m,q=map(int, input().split())
    qq=[]
    for test in range(q):
        pp=list(map(int, input().split()))
        qq.append(pp)
    qq.reverse()
    mat=[]
    for i in range(n):
        mat.append([0]*m)
    for i in range(q):
        lst = qq[i]
        if lst[0] == 3:
            mat[lst[1]-1][lst[2]-1] = lst[3]
        elif lst[0] == 2:
            d = deque([])
            for k in range(n):
                d.append(mat[k][lst[1]-1])
            d.appendleft(d.pop())
            for k in range(n):
                mat[k][lst[1]-1]=d[k]
        else:
            d = deque([])
            for k in range(m):
                d.append(mat[lst[1]-1][k])
            d.appendleft(d.pop())
            for k in range(m):
                mat[lst[1]-1][k] = d[k]
    for i in range(n):
        print(*mat[i])

main()
