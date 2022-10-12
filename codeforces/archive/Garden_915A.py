# Time: Jun/27/2022 10:46
# Title: A - Garden
# Submission ID: 161923544
# Language: Python


n,k = [int(i) for i in input().split()]
x = [int(i) for i in input().split()]
minn = 1000
for i in x:
    if k%i == 0:
        minn = min(minn, k//i)
print(minn)
