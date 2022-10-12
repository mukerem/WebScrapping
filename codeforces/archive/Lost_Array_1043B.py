# Time: Jul/19/2022 09:35
# Title: B - Lost Array
# Submission ID: 164854643
# Language: Python


arr_len = int(input())
a = [0] + [int(x) for x in input().split(" ")]
x = [0] * arr_len
res = []

for i in range(1, arr_len + 1):
    x[i-1] = a[i]-a[i-1]

def ok(k, x ,a):
    for i in range(0, arr_len):
        tmp = x[i%k] + a[i]
        if tmp != a[i + 1]:
            return False
    return True

for k in range(1, arr_len + 1):
    if ok(k, x ,a):
        res.append(str(k))

import sys
sys.stdout.write(str(len(res)) + "\n")
sys.stdout.write(" ".join(res))
