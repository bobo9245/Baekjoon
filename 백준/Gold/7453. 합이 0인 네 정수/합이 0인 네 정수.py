#걍 딕셔너리 써서 푼거(해시테이블 구현 안함)
import sys
input = sys.stdin.readline
N = int(input())
A, B, C, D = [], [], [], []
for _ in range(N):
    arr = list(map(int, input().split()))
    A.append(arr[0])
    B.append(arr[1])
    C.append(arr[2])
    D.append(arr[3])
sum_map = {}
for a in A:
    for b in B:
        sum_ab = a + b
        sum_map[sum_ab] = sum_map.get(sum_ab, 0) + 1
total_count = 0
for c in C:
    for d in D:
        target = -(c + d)
        if target in sum_map:
            total_count += sum_map[target]
print(total_count)