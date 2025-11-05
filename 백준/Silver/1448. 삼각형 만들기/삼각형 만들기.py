import sys
input=sys.stdin.readline
n=int(input())
arr=sorted([int(input()) for _ in range(n)])
#print(arr)
isover=False
if n==3:
    print(-1 if arr[0]+arr[1]<=arr[2] else sum(arr))
else:
    for i in range(n-1,1,-1):
        # print(arr[i-2]+arr[i-1],arr[i] )
        if arr[i-2]+arr[i-1]>arr[i]:
            print(sum(arr[i-2:i+1]))
            isover=True
            break
        else:
            continue
    if not isover:
        print(-1)