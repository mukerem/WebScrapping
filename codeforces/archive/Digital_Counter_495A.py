# Time: Jul/03/2022 09:47
# Title: A - Digital Counter
# Submission ID: 162611892
# Language: Python


d = {
    '0': ['0', '8'],
    '1': ['0', '1', '3', '4', '7', '8', '9'],
    '2': ['2', '8'],
    '3': ['3', '8', '9'],
    '4': ['4', '8', '9'],
    '5': ['5', '6', '8', '9'],
    '6': ['6', '8'],
    '7': ['0', '3', '7', '8', '9'],
    '8': ['8'],
    '9': ['8', '9']
    }

a = input()
b = d[a[0]]
c = d[a[1]]

ans = len(b) * len(c)
print(ans)