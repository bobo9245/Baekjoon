def find_subsequences(index, current_sum, selected, N, S, arr, count):
    if index == N:
        if selected > 0 and current_sum == S:
            count[0] += 1
        return
    find_subsequences(index + 1, current_sum + arr[index], selected + 1, N, S, arr, count)
    find_subsequences(index + 1, current_sum, selected, N, S, arr, count)

N, S = map(int, input().split())
arr = list(map(int, input().split()))
count = [0] #<<< 이거는 안에서 더해도 유지되게 하기 위해서 - global 사용해도됨
find_subsequences(0, 0, 0, N, S, arr, count)
print(count[0])