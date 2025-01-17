import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
li = [input()[0] for _ in range(n)]
count = Counter(li)
ans = [char for char in sorted(count) if count[char] >= 5 and 'a' <= char <= 'z']
print(''.join(ans) if ans else 'PREDAJA')