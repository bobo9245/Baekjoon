from itertools import combinations

# 입력 받기
N, L, R, X = map(int, input().split())
A = list(map(int, input().split()))

count = 0

# 2개 이상의 모든 조합 탐색
for i in range(2, N + 1):  # 최소 2개부터 N개까지 선택
    for subset in combinations(A, i):
        sum_val = sum(subset)
        min_val = min(subset)
        max_val = max(subset)

        if L <= sum_val <= R and (max_val - min_val) >= X:
            count += 1

# 정답 출력
print(count)