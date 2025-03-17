import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
in_degree=[0]*(n+1) # 진입차수는 여기에
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    in_degree[b]+=1


que = deque([])

for i in range(1,n+1):
    if in_degree[i]==0:
        que.append(i)

result = []
while que:
    x=que.popleft()
    result.append(x)

    for y in graph[x]:
        in_degree[y]-=1
        if in_degree[y]==0:
            que.append(y)
print(" ".join(map(str,result)))