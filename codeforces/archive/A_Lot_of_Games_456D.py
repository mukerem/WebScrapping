# Time: Jul/18/2022 22:21
# Title: D - A Lot of Games
# Submission ID: 164810752
# Language: Python


import sys, math
from sys import stdin, stdout
from operator import itemgetter

rem = 10 ** 9 + 7
take = lambda: map(int, stdin.readline().split())

def make_trie(words):
    root = {'': {}}
    for word in words:
        current_dict = root['']
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
    return root
def yes(trie,node):
    if trie[node]=={}:
        return False
    prev=False
    for child in trie[node]:
        prev|=(not yes(trie[node],child))
    return prev
def no(trie,node):
    if trie[node]=={}:
        return True
    prev=False
    for child in trie[node]:
        prev|=(not no(trie[node],child))
    return prev




arr=[]
n,k=take()
for i in range(n):
    arr.append(input())
trie=make_trie(arr)

a=yes(trie,'')
b=no(trie,'')
#print yes(trie[''],'a')
if a==True and b==True:
    print('First')
    exit()
elif a==True and b==False:
    if k%2==1:
        print ('First')
        exit()
print ('Second')
