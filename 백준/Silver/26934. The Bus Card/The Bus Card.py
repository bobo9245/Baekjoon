K=int(input())
M=K+500
dp=[99999]*(M+1)
dp[0]=0
for i in range(M+1):
    if dp[i]<99999:
        for c in[100,200,500]:
            if i+c<=M:
                dp[i+c]=min(dp[i+c],dp[i]+1)
best=(99999,99999)  # (초과분, 충전횟수)
for x in range(K,M+1):
    if dp[x]<99999:
        over=x-K
        if over<best[0] or (over==best[0] and dp[x]<best[1]):
            best=(over,dp[x])
print(best[1])
