import sys
input=sys.stdin.readline

n,k = map(int,input().split())
value=[9999999]*(k+1)
value[0]=0
arr=set({})
for _ in range(n):
    arr.add(int(input()))
arr=list(arr)
for a in arr:
    if a<=k:
        value[a]=1
for i in range(1,k+1):
    for j in range(len(arr)):
        if arr[j]<=i:
            if value[i - arr[j]] != 9999999:
                value[i] = min(value[i], value[i - arr[j]] + 1)
print(-1 if value[k]==9999999 else value[k])