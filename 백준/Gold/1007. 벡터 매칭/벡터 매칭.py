import sys
import itertools
import math

def vector_matching(points):
    n = len(points)
    total_x, total_y = sum(x for x, y in points), sum(y for x, y in points)
    min_length = float('inf')
    
    for comb in itertools.combinations(points, n // 2):
        sum_x, sum_y = sum(x for x, y in comb), sum(y for x, y in comb)
        vec_x = total_x - 2 * sum_x
        vec_y = total_y - 2 * sum_y
        min_length = min(min_length, math.sqrt(vec_x ** 2 + vec_y ** 2))

    return min_length

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
    print(f"{vector_matching(points):.6f}")