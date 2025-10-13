import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

class SegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.tree = [(0, 0)] * (4 * self.n)
        self._init(1, 0, self.n - 1)

    def _init(self, node, start, end):
        if start == end:
            self.tree[node] = (self.arr[start], self.arr[start])
            return self.tree[node]
        
        mid = (start + end) // 2
        left_child = self._init(node * 2, start, mid)
        right_child = self._init(node * 2 + 1, mid + 1, end)
        
        min_val = min(left_child[0], right_child[0])
        max_val = max(left_child[1], right_child[1])
        
        self.tree[node] = (min_val, max_val)
        return self.tree[node]

    def _query(self, node, start, end, left, right):
        if left > end or right < start:
            return (sys.maxsize, 0)
        
        if left <= start and end <= right:
            return self.tree[node]
            
        mid = (start + end) // 2
        left_res = self._query(node * 2, start, mid, left, right)
        right_res = self._query(node * 2 + 1, mid + 1, end, left, right)
        
        min_val = min(left_res[0], right_res[0])
        max_val = max(left_res[1], right_res[1])
        
        return (min_val, max_val)

    def query(self, left, right):
        return self._query(1, 0, self.n - 1, left, right)

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

segtree = SegTree(arr)

for _ in range(m):
    a, b = map(int, input().split())
    min_val, max_val = segtree.query(a - 1, b - 1)
    print(min_val, max_val)