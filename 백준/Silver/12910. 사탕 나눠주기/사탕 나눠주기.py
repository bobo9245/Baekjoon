import sys

input = sys.stdin.readline

n = int(input())
candies = list(map(int, input().split()))

brand_counts = [0] * 51
for brand in candies:
    brand_counts[brand] += 1

total_ways = 0
current_ways = 1

for k in range(1, 51):
    if brand_counts[k] == 0:
        break
    
    current_ways *= brand_counts[k]
    total_ways += current_ways

print(total_ways)