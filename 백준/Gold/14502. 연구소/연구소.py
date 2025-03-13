import sys
import itertools
import collections
import copy
input = sys.stdin.readline
n,m = map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))
empty = []
for i in range(n):
    for j in range(m):
        if arr[i][j]==0:
            empty.append([i,j])
candidates=list(itertools.combinations(empty,3))
dx=[0,0,1,-1]
dy=[1,-1,0,0]
def bfs(arr,c):
    queue=collections.deque()
    tmp = copy.deepcopy(arr)
    for x in c:
        tmp[x[0]][x[1]]=1
    for i in range(n):
        for j in range(m):
            if tmp[i][j]==2:
                queue.append((i,j))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if tmp[nx][ny]==0:
                    tmp[nx][ny]=2
                    queue.append((nx,ny))
    count=0
    for i in range(n):
        for j in range(m):
            if tmp[i][j]==0:
                count+=1
    return count
safe=0
for c in candidates:
    safe=max(safe, bfs(arr,c))

print(safe)