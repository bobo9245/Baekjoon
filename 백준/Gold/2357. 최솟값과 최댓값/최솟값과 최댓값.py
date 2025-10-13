import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

min_tree = [0] * (2 * n)
max_tree = [0] * (2 * n)

for i in range(n):
    min_tree[n + i] = arr[i]
    max_tree[n + i] = arr[i]

for i in range(n - 1, 0, -1):
    min_tree[i] = min(min_tree[i * 2], min_tree[i * 2 + 1])
    max_tree[i] = max(max_tree[i * 2], max_tree[i * 2 + 1])

def query(left, right):
    left += n
    right += n
    min_val = sys.maxsize
    max_val = 0
    
    while left < right:
        if left % 2:
            min_val = min(min_val, min_tree[left])
            max_val = max(max_val, max_tree[left])
            left += 1
        if right % 2:
            right -= 1
            min_val = min(min_val, min_tree[right])
            max_val = max(max_val, max_tree[right])
        left //= 2
        right //= 2
        
    return min_val, max_val

for _ in range(m):
    a, b = map(int, input().split())
    min_res, max_res = query(a - 1, b)
    print(min_res, max_res)