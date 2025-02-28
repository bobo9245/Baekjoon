import sys
from collections import deque

def bfs(x, y, color, grid, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue:
        curr_x, curr_y = queue.popleft()
        
        for i in range(4):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny] or grid[nx][ny] != color:
                continue
                
            visited[nx][ny] = True
            queue.append((nx, ny))

N = int(input())
grid = [list(input().strip()) for _ in range(N)]

visited_normal = [[False] * N for _ in range(N)]
normal_count = 0

for i in range(N):
    for j in range(N):
        if not visited_normal[i][j]:
            bfs(i, j, grid[i][j], grid, visited_normal)
            normal_count += 1

# Modify the grid for colorblind vision
for i in range(N):
    for j in range(N):
        if grid[i][j] == 'G':
            grid[i][j] = 'R'

visited_rg = [[False] * N for _ in range(N)]
rg_count = 0

for i in range(N):
    for j in range(N):
        if not visited_rg[i][j]:
            bfs(i, j, grid[i][j], grid, visited_rg)
            rg_count += 1

print(normal_count, rg_count)