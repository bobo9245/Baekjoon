n = int(input())
a,b = map(int, input().split())
c = int(input())
d = []
for _ in range(n):
    d.append(int(input()))
d.sort(reverse=True)

compare_kcal = c/a
total_price = a
total_kcal = c
cnt = 0
for i in range(len(d)):
    tmp = (total_kcal + d[i]) / (total_price + b)
    if tmp >=  compare_kcal:
        compare_kcal = tmp
        total_price += b
        total_kcal += d[i]
    else:
        break

print(int(total_kcal / total_price))