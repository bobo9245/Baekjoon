def total_dots_in_domino_set(N):
    return (N * (N + 1) * (N + 2)) // 2


N = int(input())
print(total_dots_in_domino_set(N))
