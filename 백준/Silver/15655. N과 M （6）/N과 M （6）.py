n,m = map(int,input().split())
ar = list(map(int,input().split()))

ar.sort()
num = []
def dfs(s):
    if len(num)==m:
        print(*num)
        return
    for i in range(s,len(ar)):
        if not ar[i] in num:
            num.append(ar[i])
            dfs(i+1)
            num.pop()
dfs(0)
        