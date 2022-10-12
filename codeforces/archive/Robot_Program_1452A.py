# Time: Jun/27/2022 14:27
# Title: A - Robot Program
# Submission ID: 161943060
# Language: Python


for _ in range(int(input())):
        x,y= [int(i) for i in input().split()]
        a = min(x, y)
        b = max(x, y)        
        moves = 2 * a
        
        # if a != b there is additional moves required
        c = b - a
        if c:
            d = 2*c - 1
            moves += d
        print(moves)
