import sys

sys.setrecursionlimit(2000)

N, R, G, B = map(int, sys.stdin.readline().split())

comb = [[0] * 11 for _ in range(11)]

for i in range(11):
    comb[i][0] = 1
    comb[i][i] = 1

for i in range(2, 11):
    for j in range(1, i):
        comb[i][j] = comb[i-1][j-1] + comb[i-1][j]

dp = [[[[-1] * 101 for _ in range(101)] for _ in range(101)] for _ in range(12)]

def find_ways(level, r, g, b):
    
    if level == N + 1:
        return 1

    if dp[level][r][g][b] != -1:
        return dp[level][r][g][b]

    k = level
    total_ways = 0

    if r >= k:
        total_ways += find_ways(level + 1, r - k, g, b)
    if g >= k:
        total_ways += find_ways(level + 1, r, g - k, b)
    if b >= k:
        total_ways += find_ways(level + 1, r, g, b - k)

    if k % 2 == 0:
        x = k // 2
        nCk = comb[k][x]
        
        if r >= x and g >= x:
            total_ways += nCk * find_ways(level + 1, r - x, g - x, b)
        if r >= x and b >= x:
            total_ways += nCk * find_ways(level + 1, r - x, g, b - x)
        if g >= x and b >= x:
            total_ways += nCk * find_ways(level + 1, r, g - x, b - x)

    if k % 3 == 0:
        x = k // 3
        ways_RGB = comb[k][x] * comb[k - x][x]
        
        if r >= x and g >= x and b >= x:
            total_ways += ways_RGB * find_ways(level + 1, r - x, g - x, b - x)

    dp[level][r][g][b] = total_ways
    return total_ways

result = find_ways(1, R, G, B)
print(result)