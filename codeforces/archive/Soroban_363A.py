# Time: Jun/27/2022 11:16
# Title: A - Soroban
# Submission ID: 161925927
# Language: Python


n = input()

def sob(a):
    d = {
        0: '-OOOO',
        1: 'O-OOO',
        2: 'OO-OO',
        3: 'OOO-O',
        4: 'OOOO-',
    }
    e = {
    0: 'O-',
    1: '-O'
    }
    return e[a//5] + '|' + d[a%5]

s=  ''
for i in n:
    x = int(i)
    s = sob(x) +'\n'+ s 
print(s)
    
    
