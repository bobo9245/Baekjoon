import sys
from collections import deque

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append([x, y])
    farm[x][y] = 0  # 방문한 지점을 0으로 바꿔 재방문 방지
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            # nx는 높이 범위, ny는 너비 범위로 조정
            if 0 <= nx < h and 0 <= ny < w and farm[nx][ny] == 1:
                farm[nx][ny] = 0
                queue.append([nx, ny])

n = int(input())
for i in range(n):
    w, h, m = map(int, input().split())
    farm = [[0] * w for _ in range(h)]  # 높이 x 너비 크기의 2차원 리스트 생성
    count = 0
    
    for j in range(m):
        a, b = map(int, input().split())
        farm[b][a] = 1  # 입력받은 위치에 배추가 있는 경우 1로 설정

    for a in range(h):  # 높이부터 반복
        for b in range(w):  # 너비 반복
            if farm[a][b] == 1:  # 배추가 있는 곳에서 BFS 시작
                bfs(a, b)
                count += 1
    print(count)
