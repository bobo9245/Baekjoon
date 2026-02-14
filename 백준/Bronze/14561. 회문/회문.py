import sys

digits = "0123456789ABCDEF"

def to_base(a, b):
    s = []
    while a:
        a, r = divmod(a, b)
        s.append(digits[r])
    return ''.join(reversed(s)) or "0"

def is_pal(s):
    return int(s == s[::-1])

input = sys.stdin.readline
t = int(input())
out = []
for _ in range(t):
    A, n = map(int, input().split())
    out.append(is_pal(to_base(A, n)))

print(*out, sep="\n")
