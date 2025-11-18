N,M=map(int,input().split())
nums=sorted(map(int,input().split()))
def dfs(depth):
    if depth == M:
        print(*li)
        return ;
    for i in range(N):
        if depth == 0 or li[-1] <= nums[i]:
            li.append(nums[i])
            dfs(depth+1)
            li.pop()
li=[]
dfs(0)