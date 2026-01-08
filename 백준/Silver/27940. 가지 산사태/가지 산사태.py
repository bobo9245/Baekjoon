import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

total_water = 0
is_collapse = False

for i in range(1, m + 1):
    t, r = map(int, input().split())
    
    total_water += r
    
    if total_water > k:
        print(i, 1)
        is_collapse = True
        break

if not is_collapse:
    print(-1)