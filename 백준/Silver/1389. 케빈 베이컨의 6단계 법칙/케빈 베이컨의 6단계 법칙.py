import sys
input = sys.stdin.readline

n, m = map(int, input().split())
INF = float('inf')
ar = [[INF] * n for _ in range(n)]

for i in range(n):
    ar[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    ar[a-1][b-1] = 1
    ar[b-1][a-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            ar[i][j] = min(ar[i][j], ar[i][k] + ar[k][j])

ans = []
for a in ar:
    ans.append(sum(a))

print(ans.index(min(ans)) + 1)