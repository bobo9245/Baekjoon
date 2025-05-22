import heapq
import sys
input = sys.stdin.readline

leftHeap = []
rightHeap = []

for i in range(int(input())):
    number = int(input())

    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, -number)
    else:
        heapq.heappush(rightHeap, number)
    
    if rightHeap and (-1 * leftHeap[0]) > rightHeap[0]:
        left_top_val = -heapq.heappop(leftHeap)
        right_top_val = heapq.heappop(rightHeap)

        heapq.heappush(leftHeap, -right_top_val)
        heapq.heappush(rightHeap, left_top_val)
        
    print(leftHeap[0] * -1)