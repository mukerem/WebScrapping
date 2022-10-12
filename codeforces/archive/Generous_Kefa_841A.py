# Time: Jul/03/2022 22:31
# Title: A - Generous Kefa
# Submission ID: 162676417
# Language: Python


n,k = [int(i) for i in input().split()]
a = list(input())

def ballon():
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    #print(d)
    for i in d.values():
        if i>k:
            return 'NO'
    return 'YES'
print(ballon())
