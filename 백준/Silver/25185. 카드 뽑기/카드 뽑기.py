import sys; input = sys.stdin.readline

def check(a, b, c):
    if a[1] == b[1] == c[1]:
        d = int(a[0]); e = int(b[0]); f = int(c[0])
        if d + 2 == e + 1 == f or d + 2 == f + 1 == e or e + 2 == d + 1 == f or e + 2 == f + 1 == d or f + 2 == d + 1 == e or f + 2 == e + 1 == d:
            return True
    return False

for _ in range(int(input())):
    a, b, c, d = input().split()
    if a == b == c or a == b == d or a == c == d or b == c == d:
        print(':)')
    elif (a == b and c == d) or (a == c and b == d) or (a == d and b == c):
        print(':)')
    elif check(a, b, c) or check(a, b, d) or check(a, c, d) or check(b, c, d):
        print(':)')
    else:
        print(':(')