# Time: Aug/05/2022 22:16
# Title: B1 - TV Subscriptions (Easy Version)
# Submission ID: 167149851
# Language: Python


for _ in range(int(input())):
    n,k,d = map(int, input().split())
    a = [int(i) for i in input().split()]
    b = {}
    for i in range(d):
        if a[i] in b:
            b[a[i]] += 1
        else:
            b[a[i]] = 1
    s = len(b)
    #print(b)
    ans = s
    for i in range(d, n):
        x = a[i-d]
        y = a[i]
        if b[x] == 1:
            b.pop(x)
            if y in b:
                b[y] += 1
                s -= 1
            else:
                b[y] = 1
        else:
            b[x] -= 1
            if y in b:
                b[y] += 1
            else:
                b[y] = 1
                s += 1
        ans = min(ans, s)
    print(ans)
                
            
        
