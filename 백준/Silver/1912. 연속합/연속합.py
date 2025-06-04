n=int(input())
arr=list(map(int,input().split()))

dp=[0]*n
for i in range(n):
    dp[i]=max(arr[i], arr[i]+dp[i-1])
print(max(dp))