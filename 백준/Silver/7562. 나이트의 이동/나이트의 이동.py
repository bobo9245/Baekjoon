import sys
from collections import deque
input=sys.stdin.readline

l = int(input())
dx = [2,2,1,1,-1,-1,-2,-2]
dy = [1,-1,2,-2,2,-2,1,-1]

def bfs(n, x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return 0
    que = deque([(x1, y1, 0)])
    visited = [[False] * n for _ in range(n)]
    visited[x1][y1] = True
    while que:
        x, y, count = que.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if nx == x2 and ny == y2:
                return count + 1
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                que.append((nx, ny, count + 1))
for _ in range(l):
    n=int(input())
    visited=[[False]*n for _ in range(n)]
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    count=bfs(n, x1,y1,x2,y2)
    print(count)