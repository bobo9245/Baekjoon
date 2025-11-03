n=int(input())
for _ in range(n):
    arr=list(map(int,input().split()))
    sum=0
    dp=[0 for i in range(len(arr))]
    dp[0],dp[1]=arr[0],arr[1]
    for i in range(2,len(arr)):
        m=0
        for j in range(i-1):
            m=max(m,dp[j])
        dp[i]=max(m+arr[i],dp[i-1])
    print(dp[len(arr)-1])