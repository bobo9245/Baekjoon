import sys
input = sys.stdin.readline

words = []

while True:
    S = input().rstrip().split(' ')
    if S[-1] == 'E-N-D':
        break
    for maybe_word in S:
        word = ''
        for char in maybe_word:
            if ('a' <= char <= 'z' or 'A' <= char <= 'Z' or '-' == char):
                word += char
        words.append(word)

print(max(words, key = lambda x: len(x)).lower())