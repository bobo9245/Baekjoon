import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())
# 1) 보석 리스트, 2) 가방 리스트
jewels = [tuple(map(int, input().split())) for _ in range(n)]
bags   = [int(input()) for _ in range(k)]

# 1) 무게 기준 오름차순 정렬
jewels.sort(key=lambda x: x[0])
# 2) 용량 기준 오름차순 정렬
bags.sort()

max_heap = []   # python heapq로 최대 힙 흉내 → (-가치)
res = 0         # 정답(총 가격 합)
i = 0           # jewels 리스트 인덱스

# 3) 작은 가방부터 순회
for cap in bags:
    # 이 가방에 들어갈 수 있는(무게 ≤ cap) 모든 보석 후보를 heap에 추가
    while i < n and jewels[i][0] <= cap:
        # 최대 힙으로 쓰려면 -가치
        heapq.heappush(max_heap, -jewels[i][1])
        i += 1

    # 후보 중 가장 비싼 보석을 꺼내어 담는다
    if max_heap:
        res += -heapq.heappop(max_heap)

print(res)
