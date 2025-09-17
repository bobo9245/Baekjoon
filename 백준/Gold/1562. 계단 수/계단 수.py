n=int(input())
dp=[[[0]*1024 for _ in range(10)] for _ in range(n+1)]
mod=1000000000
for i in range(1,10):
    dp[1][i][1<<i]=1
for length in range(2,n+1):
    for last_digit in range(10):
        for mask in range(1024):
            new_mask=mask | (1<<last_digit)
            if last_digit>0:
                dp[length][last_digit][new_mask]+=dp[length-1][last_digit-1][mask]
                dp[length][last_digit][new_mask]%=mod
            if last_digit<9:
                dp[length][last_digit][new_mask]+=dp[length-1][last_digit+1][mask]
                dp[length][last_digit][new_mask]%=mod
answer=0
final_mask=(1<<10)-1
for i in range(10):
    answer+=dp[n][i][final_mask]
    answer%=mod
print(answer)