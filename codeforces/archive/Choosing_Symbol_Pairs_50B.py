# Time: Aug/09/2022 07:33
# Title: B - Choosing Symbol Pairs
# Submission ID: 167585746
# Language: Python


def get_ordered_pairs_count(S: str) -> int:
    fre = {}
    for s in S:
        if s in fre:
            fre[s] += 1
        else:
            fre[s] = 1
    pair = 0
    for _, x in fre.items():
        pair += x*x
    return pair

s = input()
print(get_ordered_pairs_count(s))
