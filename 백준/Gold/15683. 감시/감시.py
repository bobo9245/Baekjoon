import sys
import copy

input = sys.stdin.readline

N, M = map(int, input().split())
office = []
cctvs = []

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

cctv_types = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}

for i in range(N):
    row = list(map(int, input().split()))
    office.append(row)
    for j in range(M):
        if 1 <= row[j] <= 5:
            cctvs.append((row[j], i, j))

def mark(office, x, y, dirs):
    temp_office = copy.deepcopy(office)
    for d in dirs:
        nx, ny = x, y
        while True:
            nx += directions[d][0]
            ny += directions[d][1]
            if 0 <= nx < N and 0 <= ny < M:
                if temp_office[nx][ny] == 6:
                    break
                if temp_office[nx][ny] == 0:
                    temp_office[nx][ny] = '#'
            else:
                break
    return temp_office

def dfs(depth, office):
    global min_blind_spots
    
    if depth == len(cctvs):
        blind_spots = sum(row.count(0) for row in office)
        min_blind_spots = min(min_blind_spots, blind_spots)
        return

    cctv_num, x, y = cctvs[depth]
    
    for dirs in cctv_types[cctv_num]:
        new_office = mark(office, x, y, dirs)
        dfs(depth + 1, new_office)

min_blind_spots = float('inf')

dfs(0, office)

print(min_blind_spots)
