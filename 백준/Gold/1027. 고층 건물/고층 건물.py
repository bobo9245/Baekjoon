n = int(input())
bds = list(map(int, input().split()))
ans = [0]*n

for i in range(n-1) :
    max_slope = -float('inf')
    for j in range(i+1, n) :
        slope = (bds[j] - bds[i]) / (j - i)
        if slope <= max_slope :
            continue
        max_slope = max(max_slope, slope)
        ans[i] += 1
        ans[j] += 1

print(max(ans))