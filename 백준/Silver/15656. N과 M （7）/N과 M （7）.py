import sys; input = sys.stdin.readline
def dfs():
    if len(ans) == m:
        print(*ans)
        return

    for i in num:
        ans.append(i)
        dfs()
        ans.pop()
n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
ans = []
dfs()