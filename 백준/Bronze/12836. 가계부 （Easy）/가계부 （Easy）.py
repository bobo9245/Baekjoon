n,m=map(int,input().split())
arr=[0]*n
for _ in range(m):
    query = list(map(int, input().split()))
    if query[0] == 1:
        a, b, value = query[0], query[1], query[2]
        for i in range(b - 1, n):
            arr[i] += value
    else:
        a, b, value = query[0], query[1], query[2]
        if b == 1:
            print(arr[value - 1])
        else:
            print(arr[value - 1] - arr[b - 2])