n,m=map(int,input().split())
inputarr=list(sorted(list(map(int,input().split()))))
arr=[]
def dfs(a):
    if len(arr)==m:
        print(" ".join(map(str,arr)))
        return
    else:
        for i in range(n):
            if inputarr[i] in arr:
                continue
            arr.append(inputarr[i])
            dfs(a+1)
            arr.pop()
dfs(0)