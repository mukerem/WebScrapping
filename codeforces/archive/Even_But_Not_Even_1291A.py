# Time: Jul/03/2022 19:18
# Title: A - Even But Not Even
# Submission ID: 162662873
# Language: Python


for _ in range(int(input())):
    a = int(input())
    n = input()
    x = [int(i) for i in n]
    c = 0
    ans = ''
    for i in x:
        if i % 2:
            ans += str(i)
            c += 1
        if c == 2:
            break
    if c == 2:
        print(ans)
    else:
        print(-1)
            
    
