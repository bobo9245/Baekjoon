import sys

input = sys.stdin.readline
n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]

if n == 1:
    print(0)
    sys.exit()

dp = [[0] * n for _ in range(n)]

for length in range(2, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1
        dp[i][j] = float('inf')
        
        for k in range(i, j):
            cost = dp[i][k] + dp[k + 1][j] + nums[i][0] * nums[k][1] * nums[j][1]
            if cost < dp[i][j]:
                dp[i][j] = cost

print(dp[0][n - 1])