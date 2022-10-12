# Time: Jul/12/2022 17:23
# Title: A - Ivan the Fool and the Probability Theory
# Submission ID: 163804478
# Language: Python


def random_pictures(n, m):
    mod = int(1e9 + 7)
    fib = [1,1]
    for i in range(max(n,m) + 1):
        f = fib[-1] + fib[-2]
        f = f % mod
        fib.append(f)
    picture = 2 * (fib[n] + fib[m] - 1)
    picture = picture % mod
    return picture
n,m = [int(i) for i in input().split()]
print(random_pictures(n,m))
