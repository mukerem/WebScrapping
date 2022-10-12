# Time: Jul/14/2022 16:57
# Title: B - Dima and Text Messages
# Submission ID: 164155626
# Language: Python


from typing import List
def werify_message(n:int, words: List[str], message: str) -> str:
    true_message = ''.join(['<3', '<3'.join(words), '<3'])

    # index in true_message
    i = 0
    for litera in message:
        if len(true_message) != i:
            if litera == true_message[i]:
                i += 1
        else:
            # Дошли до конца исходного сообщения и не нашли вставок
            return 'yes'

    if i == len(true_message):
        return 'yes'
    else:
        return 'no'

n = int(input())
words = list()
for i in range(n):
    word = input()
    words.append(word)

message = input()
print(werify_message(n, words, message))
