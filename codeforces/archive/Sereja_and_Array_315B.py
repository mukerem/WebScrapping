# Time: Jul/17/2022 09:47
# Title: B - Sereja and Array
# Submission ID: 164580465
# Language: Python


import sys
def main():
    n,m=list(map(int, sys.stdin.readline().split()))
    arr=[-1] + list(map(int, sys.stdin.readline().split()))
    cnt=0
    for i in range(m):
        op=list(map(int, sys.stdin.readline().split()))
        if op[0]==1:
            arr[op[1]]=op[2]-cnt
        elif op[0]==2:
            cnt+=op[1]
        else:
            print(arr[op[1]]+cnt)
main()
