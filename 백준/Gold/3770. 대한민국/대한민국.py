import sys

# 입력을 한 번에 읽어와서 처리 (속도 최적화)
input_data = sys.stdin.read().split()
if not input_data:
    exit()

ptr = 0
T_cases = int(input_data[ptr])
ptr += 1

for t in range(1, T_cases + 1):
    N = int(input_data[ptr])
    M = int(input_data[ptr + 1])
    K = int(input_data[ptr + 2])
    ptr += 3
    
    roads = []
    for _ in range(K):
        u = int(input_data[ptr])
        v = int(input_data[ptr + 1])
        roads.append((u, v))
        ptr += 2
        
    # 1. 동해안 도시(u) 기준 오름차순, 같으면 서해안(v) 기준 오름차순 정렬
    roads.sort()
    
    # 2. 반복문 기반 세그먼트 트리 설정 (1 ~ M 범위)
    size = 1
    while size < M:
        size *= 2
    tree = [0] * (2 * size)
    
    def update(i, val):
        idx = i + size - 1
        while idx > 0:
            tree[idx] += val
            idx //= 2
            
    def query(l, r):
        res = 0
        l += size - 1
        r += size - 1
        while l <= r:
            if l % 2 == 1:
                res += tree[l]
                l += 1
            if r % 2 == 0:
                res += tree[r]
                r -= 1
            l //= 2
            r //= 2
        return res

    ans = 0
    # 3. 도로를 하나씩 확인하며 교차점 계산
    for u, v in roads:
        # 현재 도로의 서해안 번호 v보다 큰 번호가 이미 몇 개 들어왔는지 확인
        if v < M:
            ans += query(v + 1, M)
        # 현재 도로의 서해안 번호를 트리에 기록
        update(v, 1)
        
    sys.stdout.write(f"Test case {t}: {ans}\n")