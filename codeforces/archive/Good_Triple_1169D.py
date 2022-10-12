# Time: Aug/06/2022 11:57
# Title: D - Good Triple
# Submission ID: 167198514
# Language: Python


s = input()
n = len(s)
v = [n] * (n+1)
ans = 0
for i in range(n-1, -1,-1):
    v[i] = v[i + 1]
    k = 1
    while i + 2 * k < v[i]:
        if (s[i] == s[i + k] and s[i + k] == s[i + 2 * k]):
            v[i] = i + 2 * k
        k += 1
    ans += n - v[i]
print(ans)
