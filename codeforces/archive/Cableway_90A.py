# Time: Jul/03/2022 18:28
# Title: A - Cableway
# Submission ID: 162658649
# Language: Python


r,g,b = [int(i) for i in input().split()]

x = 30 + 3 * ((r+1)//2 - 1) + 0
y = 30 + 3 * ((g+1)//2 - 1) + 1
z = 30 + 3 * ((b+1)//2 - 1) + 2
print(max(x,y,z))
