import sys
import math
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance_squared = (x2 - x1) ** 2 + (y2 - y1) ** 2
    sum_squared = (r1 + r2) ** 2
    diff_squared = (r1 - r2) ** 2
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif sum_squared == distance_squared or diff_squared == distance_squared:
        print(1)
    elif diff_squared < distance_squared < sum_squared:
        print(2)
    else:
        print(0)
