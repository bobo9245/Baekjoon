import heapq
import sys

input = sys.stdin.readline

n = int(input())
if n == 1:
    print(0)
else:
    cards = []
    
    for _ in range(n):
        heapq.heappush(cards, int(input()))

    total = 0

    while len(cards) > 1:
        current_sum = heapq.heappop(cards) + heapq.heappop(cards)
        total += current_sum
        heapq.heappush(cards, current_sum)

    print(total)
