# Time: Jun/30/2022 11:13
# Title: A - Cutting Banner
# Submission ID: 162314696
# Language: Python


def is_cut_possible(word: str) -> bool:
    # Check CODEFORCES is found in the end of the string
    if word[:10] == 'CODEFORCES':
        return True
    if word[-10: ] == 'CODEFORCES':
        return True
    
    # check two partiton of the word which is the first i characters and the last 10-i characters.
    code = 'CODEFORCES'
    for i in range(1, 10):
        if word[:i] == code[:i] and word[i-10:] == code[i-10:]:
            return True
    return False
s = input()
print("YES" if is_cut_possible(s) else "NO")
