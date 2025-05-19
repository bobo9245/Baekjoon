import sys

N = int(sys.stdin.readline())

liquids = list(map(int, sys.stdin.readline().split()))

left, right = 0, N - 1

min_abs_sum = float('inf')
best_left_val = 0
best_right_val = 0

while left < right:
    current_sum = liquids[left] + liquids[right]
    current_abs_sum = abs(current_sum)

    if current_abs_sum < min_abs_sum:
        min_abs_sum = current_abs_sum
        best_left_val = liquids[left]
        best_right_val = liquids[right]

    if current_sum == 0:
        break
    elif current_sum < 0:
        left += 1
    else:
        right -= 1

print(best_left_val, best_right_val)