import sys
input = sys.stdin.readline

N = int(input())
F = [0] * (N + 3)
F[1] = F[2] = 1
for i in range(3, N + 3):
    F[i] = F[i-1] + F[i-2]

S = F[N+2] - 1

M = N
if S % 2 != 0:
    S -= F[N]
    M = N - 1

target = S // 2

used = [False] * (N + 1)
A = []
for i in range(M, 0, -1):
    if F[i] <= target:
        A.append(i)
        used[i] = True
        target -= F[i]
        if target == 0:
            break
B = [i for i in range(1, M+1) if not used[i]]
print(len(A))
print(*A)
print(len(B))
print(*B)