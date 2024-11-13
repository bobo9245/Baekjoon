def min_road_load_optimized(c, w):
    base_cars_per_road = c // w
    remainder = c % w
    load = (w - remainder) * (base_cars_per_road ** 2) + remainder * ((base_cars_per_road + 1) ** 2)
    return load

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
w = list(map(int, input().split()))
v = [0] * (n - 1)

for i in range(m):
    a, b, x = map(int, input().split())
    v[a - 1] += x
    if b < n:
        v[b - 1] -= x

for i in range(1, n - 1):
    v[i] += v[i - 1]

for i in range(n - 1):
    print(min_road_load_optimized(v[i], w[i]))
