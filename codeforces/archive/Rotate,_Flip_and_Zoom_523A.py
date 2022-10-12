# Time: Jul/12/2022 18:56
# Title: A - Rotate, Flip and Zoom
# Submission ID: 163902066
# Language: Python


'''from typing import List

def rotate_flip_zoom(w: int, h: int, a: List[str]) -> List[str]:
    new = [ [None] * (2*h) for i in range(2*w)] # create new array to store the image the new dimension is 2h by 2w
    for i in range(h):
        for j in range(w):
            new[2*(w-j-1)+1][2*(h-i-1)+1] = a[i][j]
            new[2*(w-j-1)+1][2*(h-i-1)] = a[i][j]
            new[2*(w-j-1)][2*(h-i-1)+1] = a[i][j]
            new[2*(w-j-1)][2*(h-i-1)] = a[i][j]
    return [''.join(row) for row in new] # concatinate each row
'''
from typing import List

def rotate_flip_zoom(w: int, h: int, a: List[str]) -> List[str]:
    new = [ ['.'] * (2*h) for i in range(2*w)] # create new array to store the image the new dimension is 2h by 2w
    for i in range(h):
        for j in range(w):
            new[2*j+1][2*i+1] = a[i][j]
            new[2*j+1][2*i] = a[i][j]
            new[2*j][2*i+1] = a[i][j]
            new[2*j][2*i] = a[i][j]
    return [''.join(row) for row in new] # concatinate each row
w,h = [int(i) for i in input().split()]
x  = []
for i in range(h):
    x.append(list(input()))
y = rotate_flip_zoom(w, h, x)
for i in y:
    print(i)
