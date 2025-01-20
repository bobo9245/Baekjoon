n = int(input())
ar = []
for i in range(n):
    ar.append(list(input()))
for i in range(n):
    for j in range(n):
        ar[i][j] = 0 if ar[i][j] == 'N' else 1

ans = 0
for c in range(n):
    friend = set()
    for i in range(n):
        if ar[c][i] == 1:
            friend.add(i)
            for j in range(n):
                if ar[i][j] == 1 and j != c:
                    friend.add(j)
    ans = max(ans, len(friend))
print(ans)