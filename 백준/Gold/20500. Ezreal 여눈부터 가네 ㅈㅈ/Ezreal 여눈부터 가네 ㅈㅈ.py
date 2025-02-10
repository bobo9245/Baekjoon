n = int(input())
MOD = 1000000007

dp =[[0]*3 for i in range(1516)]

dp[1][1] = 1
dp[1][2] = 1

for i in range(2, n+1):
    dp[i][0] = dp[i-1][2] + dp[i-1][1]
    dp[i][1] = dp[i-1][0] + dp[i-1][2]
    dp[i][2] = dp[i-1][1] + dp[i-1][0]

ans = dp[n-1][1] % MOD
print(ans)