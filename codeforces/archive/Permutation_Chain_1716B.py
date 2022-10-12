# Time: Aug/04/2022 17:52
# Title: B - Permutation Chain
# Submission ID: 166954999
# Language: Python


for _ in range(int(input())):
    n = int(input())
    a = [i for i in range(1, n+1)]
    print(n)
    k = 0
    print(*a)
    for i in range(n-1):
        a[k], a[k+1] = a[k+1], a[k]
        k += 1
        print(*a)
        '''
        z = 0
        for idx, v in enumerate(a):
            if idx + 1 == v:
                z+=1
        print(z)
        '''
