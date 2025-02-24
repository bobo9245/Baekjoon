import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())

count = 0

def func(n, r, c):
    global count
    if n == 0:
        print(count)
        return
    
    size = 2 ** (n - 1)
    yover = 1 if (r >= size) else 0
    xover = 1 if (c >= size) else 0
    
    quadrant = 2 * yover + xover
    count += quadrant * (size ** 2)

    r -= size * yover
    c -= size * xover
    
    func(n - 1, r, c)

func(n, r, c)
