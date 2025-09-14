import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

m,n=map(int,input().split())
arr=[list(map(int,input().split())) for i in range(m)]
dp=[[-1]*n for i in range(m)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def solution(x,y):
    if x==m-1 and y==n-1:
        return 1
    if dp[x][y]==-1:
        dp[x][y]=0
        for i in range(4):
            ddx,ddy=x+dx[i],y+dy[i]
            if 0<=ddx<m and 0<=ddy<n and arr[ddx][ddy]<arr[x][y]:
                dp[x][y]+=solution(ddx,ddy)
    return dp[x][y]
print(solution(0,0))