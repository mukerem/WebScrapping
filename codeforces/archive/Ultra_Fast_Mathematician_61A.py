# Time: Jul/03/2022 17:07
# Title: A - Ultra-Fast Mathematician
# Submission ID: 162651374
# Language: Python


a = input()
b = input()
c = ''
for i,j in zip(a, b):
    if i == j:
        c += '0'
    else:
        c += '1'
print(c)
