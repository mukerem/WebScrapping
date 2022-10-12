# Time: 2022-09-21 12:51:19
# title: Divisor Shuffle
# language: Python 3


n = int(input())
a = [int(i) for i in input().split()]
a.sort(reverse=True)
x = a[0]
for i in range(n-1):
    if x%a[i] != 0:
        y = a[i]
        break
    else:
        if a[i] == a[i+1]:
            y = a[i]
            break
print(y, x)
        