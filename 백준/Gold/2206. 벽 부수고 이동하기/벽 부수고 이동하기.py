import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
zido = [list(map(int, input().strip())) for _ in range(n)]

visited = [[[False]*2 for _ in range(m)] for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    que = deque()
    que.append((0, 0, 1, 0))  # x, y, distance, wallbreak
    visited[0][0][0] = True

    while que:
        x, y, dis, wallbreak = que.popleft()

        if x == n - 1 and y == m - 1:
            print(dis)
            return

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m:
                if zido[nx][ny] == 0 and not visited[nx][ny][wallbreak]:
                    visited[nx][ny][wallbreak] = True
                    que.append((nx, ny, dis + 1, wallbreak))
                elif zido[nx][ny] == 1 and wallbreak == 0 and not visited[nx][ny][1]:
                    visited[nx][ny][1] = True
                    que.append((nx, ny, dis + 1, 1))
    
    print(-1)

bfs()
