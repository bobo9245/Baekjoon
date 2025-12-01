N = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
sum = 0
score = 0
total = 0
for i in range(0, N-1):
    score = a[i] * a[i+1]
    a[i+1] = a[i] + a[i+1]
    total = total + score
print(total)