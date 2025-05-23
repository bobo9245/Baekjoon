import sys
import copy

# 입력 받기
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

# 왼쪽으로 이동 및 병합
def left(board):
    new_board = copy.deepcopy(board) # 원본 보드를 변경하지 않도록 복사본 사용
    for i in range(n):
        cursor = 0
        for j in range(1, n):
            if new_board[i][j] != 0:
                tmp = new_board[i][j]
                new_board[i][j] = 0

                if new_board[i][cursor] == 0:
                    new_board[i][cursor] = tmp
                elif new_board[i][cursor] == tmp:
                    new_board[i][cursor] *= 2
                    cursor += 1
                else:
                    cursor += 1
                    new_board[i][cursor] = tmp
    return new_board

# 오른쪽으로 이동 및 병합
def right(board):
    new_board = copy.deepcopy(board) # 원본 보드를 변경하지 않도록 복사본 사용
    for i in range(n):
        cursor = n - 1
        for j in range(n - 2, -1, -1): # n-2부터 0까지 역순으로 탐색
            if new_board[i][j] != 0:
                tmp = new_board[i][j]
                new_board[i][j] = 0

                if new_board[i][cursor] == 0:
                    new_board[i][cursor] = tmp
                elif new_board[i][cursor] == tmp:
                    new_board[i][cursor] *= 2
                    cursor -= 1
                else:
                    cursor -= 1
                    new_board[i][cursor] = tmp
    return new_board

# 위쪽으로 이동 및 병합
def up(board):
    new_board = copy.deepcopy(board) # 원본 보드를 변경하지 않도록 복사본 사용
    for i in range(n):
        cursor = 0
        for j in range(1, n):
            if new_board[j][i] != 0:
                tmp = new_board[j][i]
                new_board[j][i] = 0

                if new_board[cursor][i] == 0:
                    new_board[cursor][i] = tmp
                elif new_board[cursor][i] == tmp:
                    new_board[cursor][i] *= 2
                    cursor += 1
                else:
                    cursor += 1
                    new_board[cursor][i] = tmp
    return new_board

# 아래쪽으로 이동 및 병합
def down(board):
    new_board = copy.deepcopy(board) # 원본 보드를 변경하지 않도록 복사본 사용
    for i in range(n):
        cursor = n - 1
        for j in range(n - 2, -1, -1): # n-2부터 0까지 역순으로 탐색
            if new_board[j][i] != 0:
                tmp = new_board[j][i]
                new_board[j][i] = 0

                if new_board[cursor][i] == 0:
                    new_board[cursor][i] = tmp
                elif new_board[cursor][i] == tmp:
                    new_board[cursor][i] *= 2
                    cursor -= 1
                else:
                    cursor -= 1
                    new_board[cursor][i] = tmp
    return new_board

max_val = 0 # 'max' 대신 'max_val' 사용 (내장 함수 충돌 방지)

# 깊이 우선 탐색(DFS)으로 모든 경우 탐색
def dfs(m, mat):
    global max_val
    # 5번 이동했으면 최댓값 갱신 후 종료
    if m == 5:
        for i in range(n):
            for j in range(n):
                if mat[i][j] > max_val:
                    max_val = mat[i][j]
        return

    # 4가지 방향(상, 하, 좌, 우)으로 이동 시도
    # 각 방향으로 이동 시, 현재 보드(mat)의 복사본을 넘겨줌
    dfs(m + 1, left(mat))
    dfs(m + 1, right(mat))
    dfs(m + 1, up(mat))
    dfs(m + 1, down(mat))

# DFS 시작
dfs(0, arr)
# 최댓값 출력
print(max_val)