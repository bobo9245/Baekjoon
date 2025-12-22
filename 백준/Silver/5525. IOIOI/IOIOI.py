import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().rstrip()

ans = 0
count = 0
i = 1

while i < (M - 1):
    if S[i-1] == 'I' and S[i] == 'O' and S[i+1] == 'I':
        count += 1
        if count >= N:
            ans += 1
        i += 2
    else:
        count = 0
        i += 1

print(ans)