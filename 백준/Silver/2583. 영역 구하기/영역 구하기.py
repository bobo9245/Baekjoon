from collections import deque
m,n,k = map(int,input().split())

arr=[[0]*n for _ in range(m)]
visited=[[False]*n for _ in range(m)]
for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            arr[j][i]=1

dx=[1,-1,0,0]
dy=[0,0,1,-1]
def bfs(i, j):
    area = 1 
    que = deque([(i, j)])
    visited[i][j] = True 

    while que:
        x, y = que.popleft()
        for d in range(4): 
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < m and 0 <= ny < n: 
                if not visited[nx][ny] and arr[nx][ny] == 0:
                    que.append((nx, ny))
                    visited[nx][ny] = True
                    area += 1

    return area
            

count=0
area=[]
for i in range(m):
    for j in range(n):
        if arr[i][j]==0 and visited[i][j]==False:
            count+=1
            area.append(bfs(i,j))
print(count)
print(" ".join(map(str,list(sorted((area))))))