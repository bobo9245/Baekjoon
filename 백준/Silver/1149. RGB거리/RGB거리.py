import sys
input = sys.stdin.readline
n = int(input())
ar=[]
for i in range(n):
    ar.append(list(map(int,input().split())))
dp = [[99999]*3 for i in range(n)]
dp[0] = ar[0]
for i in range(1,n):
    dp[i][0]=ar[i][0]+min(dp[i-1][1],dp[i-1][2])
    dp[i][1]=ar[i][1]+min(dp[i-1][0],dp[i-1][2])
    dp[i][2]=ar[i][2]+min(dp[i-1][0],dp[i-1][1])
print(min(dp[-1]))