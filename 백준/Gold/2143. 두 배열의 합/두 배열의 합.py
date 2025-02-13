import sys
import bisect

input = sys.stdin.readline

def get_subarray_sums(arr):
    n = len(arr)
    sub_sums = []
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            sub_sums.append(current_sum)
    return sub_sums

def main():
    T = int(input().strip())
    n = int(input().strip())
    A = list(map(int, input().split()))
    m = int(input().strip())
    B = list(map(int, input().split()))
    
    subA = get_subarray_sums(A)
    subB = get_subarray_sums(B)
    subB.sort()  # 이진 탐색을 위해 정렬
    
    count = 0
    for a in subA:
        # 목표값 T를 만들기 위한 B의 부분합: target = T - a
        target = T - a
        left = bisect.bisect_left(subB, target)
        right = bisect.bisect_right(subB, target)
        count += (right - left)
    
    print(count)

if __name__ == '__main__':
    main()
