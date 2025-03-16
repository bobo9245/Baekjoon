from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def bfs(arr, visited, i, j, m, n):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    while queue:
        x, y = queue.popleft()
        for d in range(8):
            xx = x + dx[d]
            yy = y + dy[d]
            if 0 <= xx < m and 0 <= yy < n:
                if arr[xx][yy] == 1 and not visited[xx][yy]:
                    visited[xx][yy] = True
                    queue.append((xx, yy))

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    # 전체 m행의 배열을 입력받음
    arr = [list(map(int, input().split())) for _ in range(m)]
    visited = [[False] * n for _ in range(m)]
    count = 0

    # 행은 m, 열은 n으로 순회
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1 and not visited[i][j]:
                bfs(arr, visited, i, j, m, n)
                count += 1
    print(count)
