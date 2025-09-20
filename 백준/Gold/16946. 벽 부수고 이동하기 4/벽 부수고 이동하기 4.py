import sys
from collections import deque

def bfs(r, c, group_id):
    q = deque([(r, c)])
    visited[r][c] = True
    groups[r][c] = group_id
    count = 1
    
    while q:
        curr_r, curr_c = q.popleft()
        
        for i in range(4):
            next_r, next_c = curr_r + dr[i], curr_c + dc[i]
            
            if 0 <= next_r < n and 0 <= next_c < m:
                if not visited[next_r][next_c] and board[next_r][next_c] == '0':
                    visited[next_r][next_c] = True
                    groups[next_r][next_c] = group_id
                    q.append((next_r, next_c))
                    count += 1
    return count

input = sys.stdin.readline
n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]

visited = [[False] * m for _ in range(n)]
groups = [[0] * m for _ in range(n)]
group_sizes = {}
group_id_counter = 1

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if board[i][j] == '0' and not visited[i][j]:
            size = bfs(i, j, group_id_counter)
            group_sizes[group_id_counter] = size
            group_id_counter += 1

result = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j] == '1':
            total = 1
            neighbor_groups = set()
            for k in range(4):
                ni, nj = i + dr[k], j + dc[k]
                
                if 0 <= ni < n and 0 <= nj < m and groups[ni][nj] != 0:
                    neighbor_groups.add(groups[ni][nj])
            
            for group_id in neighbor_groups:
                total += group_sizes[group_id]
            
            result[i][j] = total % 10

for row in result:
    print("".join(map(str, row)))