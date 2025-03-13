from itertools import combinations
from collections import deque

# 입력 받기
n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

empty = [(i, j) for i in range(n) for j in range(m) if lab[i][j] == 0]
virus = [(i, j) for i in range(n) for j in range(m) if lab[i][j] == 2]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque(virus)
    temp = [row[:] for row in lab]  # 간단한 슬라이싱 복사 사용 (deepcopy보다 빠름)

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and temp[nx][ny] == 0:
                temp[nx][ny] = 2
                queue.append((nx, ny))

    # 안전 영역 크기 계산
    return sum(row.count(0) for row in temp)

# 벽 세우기 (조합 이용)
max_safe_area = 0
for walls in combinations(empty, 3):
    for wx, wy in walls:
        lab[wx][wy] = 1  # 벽 세우기

    max_safe_area = max(max_safe_area, bfs())

    for wx, wy in walls:
        lab[wx][wy] = 0  # 벽 철거 (원상 복구)

print(max_safe_area)
