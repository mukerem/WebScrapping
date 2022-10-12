# Time: 2022-09-06 00:09:28
# title: The Weight Of Words
# language: Python 3


l, w = map(int, input().split())
if w < l or w > l*26:
    print('impossible')
else:
    a = [w//l for i in range(l)]
    r = w%l
    for i in range(r):
        a[i] += 1
    s = ''
    for i in a:
        s += chr(96+i)
    print(s)