import heapq


N, M = map(int, input().split())
dict_set = set()
alphabet = [-1] * 26
order = [[] for _ in range(N)]

able = True

for i in range(1, M + 1):
    snupti = input()

    if snupti in dict_set:
        able = False
    else:
        dict_set.add(snupti)

    if not able:
        continue

    for n in range(N):
        char_index = ord(snupti[n]) - ord('A')
        if alphabet[char_index] == -1:
            alphabet[char_index] = n
            heapq.heappush(order[n], snupti[n])
        elif alphabet[char_index] != n:
            able = False

if not able:
    print("NO")
else:
    total = 1
    for q in order:
        total *= len(q)

    if total != M:
        print("NO")
    else:
        print("YES")
        for q in order:
            while q:
                print(heapq.heappop(q), end="")
            print()