MOD = 10**9 + 7

# 입력 받기
N = int(input())
A = list(map(int, input().split()))

# 세그먼트 트리의 크기는 (값의 범위)에 맞춰 결정 (여기서는 A의 값이 1 이상이라 가정)
size = max(A)  # 필요에 따라 좌표 압축할 수 있음
# 트리의 각 노드에는 길이 11의 배열을 저장 (인덱스 0은 길이 1, ..., 인덱스 10은 길이 11)
tree = [[0] * 11 for _ in range(2 * size)]

def update(idx, depth, val):
    # idx: 업데이트할 위치 (0-based)
    idx += size
    while idx:
        tree[idx][depth] = (tree[idx][depth] + val) % MOD
        idx //= 2

def query(left, right, depth):
    # 구간 [left, right]에서 depth에 해당하는 값의 합을 구함.
    res = 0
    left += size
    right += size
    while left <= right:
        if left % 2 == 1:
            res = (res + tree[left][depth]) % MOD
            left += 1
        if right % 2 == 0:
            res = (res + tree[right][depth]) % MOD
            right -= 1
        left //= 2
        right //= 2
    return res

# 수열을 순회하면서 DP 처리
for x in A:
    # x의 값에 해당하는 인덱스는 x-1 (0-based)
    pos = x - 1
    # 길이 1인 증가 수열: 항상 1
    update(pos, 0, 1)
    # 길이 2부터 11까지 처리
    for depth in range(1, 11):
        # A[i]보다 작은 값들에 대해, 이전 길이 (depth-1)에 해당하는 합 구하기
        if pos - 1 >= 0:
            cnt = query(0, pos - 1, depth - 1)
        else:
            cnt = 0
        # 구한 개수로 업데이트
        update(pos, depth, cnt)

# 최종적으로 트리의 루트에 저장된 길이 11 (depth 10)에 대한 누적합이 전체 개수
result = tree[1][10] % MOD
print(result)
