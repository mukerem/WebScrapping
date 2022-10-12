# Time: Aug/09/2022 09:53
# Title: B - Game with string
# Submission ID: 167596368
# Language: Python


def string_game(game: str) -> str:
    count = []
    c = 1
    for i in range(len(game) -1):
        if game[i] == game[i+1]:
            c += 1
        else:
            count.append([c, game[i]])
            c = 1
    count.append([c, game[-1]])
    
    stack = []
    n = 0
    turn = 0
    for c, s in count:
        #print(stack, c, s, turn)
        if c % 2 == 0:
            turn += c // 2
            continue
        if n == 0:
            stack.append([c, s])
            n += 1
            continue
            
        top = stack[-1]
        if top[1] == s:
            turn += (top[0] + c) // 2
            stack.pop()
            n -= 1
        else:
            stack.append([c, s])
            n += 1
        #print('**', stack, turn)
    for c, s in stack:
        turn += c // 2
    if turn % 2 == 0:
        return "NO"
    return "YES"

s = input()
print(string_game(s))
