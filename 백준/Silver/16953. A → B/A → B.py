from collections import deque

A, B = map(int, input().split())
queue = deque()
visited = dict()

queue.append(A)
visited[A] = 0

while queue:
    cur = queue.popleft()
    if cur == B:
        break

    for next_val in [cur * 2, cur * 10 + 1]:
        if next_val <= B and next_val not in visited:
            visited[next_val] = visited[cur] + 1
            queue.append(next_val)

print(visited[B] + 1 if B in visited else -1)
