def find_round(N, kim, lim):
    round = 0
    while kim != lim:
        kim = (kim + 1) // 2
        lim = (lim + 1) // 2
        round += 1
    return round
N, kim, lim = map(int, input().split())
print(find_round(N, kim, lim))
