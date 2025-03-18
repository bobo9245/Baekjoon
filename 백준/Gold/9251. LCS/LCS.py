import sys
input = sys.stdin.readline

arr1 = list(input().strip())
arr2 = list(input().strip())
n, m = len(arr1), len(arr2)
arr = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if arr1[i - 1] == arr2[j - 1]:
            arr[i][j] = arr[i - 1][j - 1] + 1
        else:
            arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])

print(arr[n][m])
