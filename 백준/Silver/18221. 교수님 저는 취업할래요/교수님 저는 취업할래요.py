import math

def solve():
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]

    p_r, p_c = -1, -1
    s_r, s_c = -1, -1

    for r in range(n):
        for c in range(n):
            if grid[r][c] == 5:
                p_r, p_c = r, c
            elif grid[r][c] == 2:
                s_r, s_c = r, c

    distance = math.sqrt((p_r - s_r)**2 + (p_c - s_c)**2)

    min_r, max_r = min(p_r, s_r), max(p_r, s_r)
    min_c, max_c = min(p_c, s_c), max(p_c, s_c)

    student_count = 0
    for r in range(min_r, max_r + 1):
        for c in range(min_c, max_c + 1):
            if grid[r][c] == 1:
                student_count += 1
    
    if distance >= 5 and student_count >= 3:
        print(1)
    else:
        print(0)

solve()